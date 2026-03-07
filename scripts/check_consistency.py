#!/usr/bin/env python3
"""
check_consistency.py
--------------------
Analyses HPSWG-Models TSV files for consistency of inter-model linking nodes.

Strategy (Phase 1)
------------------
Each formed model should declare a '//subgraph Linked Entities' block listing
the nodes that connect it to other models. These are the only nodes checked for
consistency -- high-multiplicity classes like E55 (type terms) and EX_Digital_Image
are ignored unless they appear explicitly in a Linked Entities block.

The checker:
  1. Extracts the key entity (first subject node) and Linked Entities block from
     each model file.
  2. Builds a cross-model index of linked entity nodes by class code.
  3. Reports three categories:
       A. Workflow conflicts -- linked entity label differs from workflow canonical label.
       B. Inter-model disagreements -- two or more models disagree, no workflow reference.
       C. Models missing the Linked Entities subgraph.

Workflow TSVs (models/workflows/) are treated as the canonical reference.
User workflow TSVs (models/user_workflows/) are excluded entirely.

Output: reports/consistency_report.md
"""

import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, NamedTuple, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Paths and constants
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = REPO_ROOT / "models"
REPORTS_DIR = REPO_ROOT / "reports"
REPORT_FILE = REPORTS_DIR / "consistency_report.md"

EXCLUDED_FOLDERS = {"old_samples", "user_workflows"}
WORKFLOW_FOLDERS = {"workflows"}

VERSION_RE = re.compile(r"_v(\d+(?:\.\d+)*)\.tsv$")
SKIP_RE = re.compile(r"^\s*//")
SUBGRAPH_START_RE = re.compile(r"^\s*//subgraph\s+Linked Entities", re.IGNORECASE)
SUBGRAPH_END_RE = re.compile(r"^\s*//end", re.IGNORECASE)
INSTANCE_SUFFIX_RE = re.compile(r"#-\d+$")

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

class ModelFile(NamedTuple):
    path: Path
    folder: str
    is_workflow: bool


class ModelAnalysis(NamedTuple):
    model_file: ModelFile
    key_entity: Optional[str]        # canonical label of first subject node
    linked_entities: List[str]       # canonical labels from Linked Entities block
    has_linked_entities_block: bool  # whether the block was found at all


class LinkedNode(NamedTuple):
    class_code: str
    label: str                       # everything after "CODE: "
    full_name: str                   # original canonical node name


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_version(filename: str) -> Optional[Tuple[int, ...]]:
    m = VERSION_RE.search(filename)
    if not m:
        return None
    try:
        return tuple(int(p) for p in m.group(1).split("."))
    except ValueError:
        return None


def short_name(path: Path) -> str:
    return f"{path.parent.name}/{path.name}"


def strip_instance_suffix(name: str) -> str:
    return INSTANCE_SUFFIX_RE.sub("", name).strip()


def extract_class_code(name: str) -> Optional[str]:
    """
    Extract CRM class code from a node name.
    'E22: Heritage Object' -> 'E22'
    'S13/E19: Sample'      -> 'S13/E19'
    Returns None if no recognisable prefix.
    """
    parts = name.split(":", 1)
    if len(parts) < 2:
        return None
    candidate = parts[0].strip()
    if re.match(r"^[A-Za-z][A-Za-z0-9_/]*$", candidate):
        return candidate
    return None


def extract_label(name: str) -> str:
    """Everything after the first colon, stripped."""
    parts = name.split(":", 1)
    return parts[1].strip() if len(parts) > 1 else name


def to_linked_node(raw_name: str) -> Optional[LinkedNode]:
    """Convert a raw node name to a LinkedNode, or None if not a CRM node."""
    canonical = strip_instance_suffix(raw_name.strip())
    code = extract_class_code(canonical)
    if code is None:
        return None
    label = extract_label(canonical)
    return LinkedNode(class_code=code, label=label, full_name=canonical)


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def latest_tsv_in_folder(folder: Path) -> Optional[Path]:
    versioned = [
        (parse_version(p.name), p)
        for p in folder.glob("*_v*.tsv")
        if parse_version(p.name) is not None
    ]
    if not versioned:
        return None
    versioned.sort(reverse=True, key=lambda vp: vp[0])
    return versioned[0][1]


def discover_model_files() -> List[ModelFile]:
    files: List[ModelFile] = []
    if not MODELS_DIR.exists():
        return files
    for child in sorted(MODELS_DIR.iterdir()):
        if not child.is_dir() or child.name in EXCLUDED_FOLDERS:
            continue
        latest = latest_tsv_in_folder(child)
        if latest is not None:
            files.append(ModelFile(
                path=latest,
                folder=child.name,
                is_workflow=child.name in WORKFLOW_FOLDERS,
            ))
    return files


# ---------------------------------------------------------------------------
# TSV parsing
# ---------------------------------------------------------------------------

def parse_model_file(mf: ModelFile) -> ModelAnalysis:
    """
    Extract the key entity and Linked Entities block from a TSV file.

    Key entity: the subject of the first non-comment, non-directive triple.
    Linked Entities: all Subject values declared as nodes inside the
      '//subgraph Linked Entities ... //end' block.
    """
    try:
        lines = mf.path.read_text(encoding="utf-8").splitlines()
    except Exception as e:
        print(f"Warning: could not read {mf.path}: {e}", file=sys.stderr)
        return ModelAnalysis(mf, None, [], False)

    key_entity: Optional[str] = None
    linked_entities: List[str] = []
    in_linked_block = False
    has_linked_block = False

    for line in lines:
        # Detect subgraph markers
        if SUBGRAPH_START_RE.match(line):
            in_linked_block = True
            has_linked_block = True
            continue
        if SUBGRAPH_END_RE.match(line) and in_linked_block:
            in_linked_block = False
            continue

        # Skip all other directives and comments
        if SKIP_RE.match(line):
            continue

        parts = line.split("\t")
        if len(parts) < 3:
            continue

        subj_raw = parts[0].strip()
        pred = parts[1].strip().lower()
        if not subj_raw or not pred:
            continue

        # Skip metadata predicates
        if pred in ("tooltip", "has note", "from list"):
            continue

        canonical_subj = strip_instance_suffix(subj_raw)

        # Key entity: first subject seen in the whole file
        if key_entity is None and not in_linked_block:
            if extract_class_code(canonical_subj) is not None:
                key_entity = canonical_subj

        # Linked entities: subjects declared inside the block
        if in_linked_block:
            if extract_class_code(canonical_subj) is not None:
                if canonical_subj not in linked_entities:
                    linked_entities.append(canonical_subj)

    return ModelAnalysis(
        model_file=mf,
        key_entity=key_entity,
        linked_entities=linked_entities,
        has_linked_entities_block=has_linked_block,
    )


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def analyse(analyses: List[ModelAnalysis]) -> Dict:
    """
    Build the consistency index from parsed model analyses.

    Returns:
      workflow_nodes    -- {class_code -> set of labels} from workflow files
      model_nodes       -- {class_code -> {label -> set of short_names}}
                           from individual (non-workflow) models
      workflow_conflicts -- per model: nodes whose label differs from workflow canonical
      inter_model_disagreements -- class codes with >1 label, no workflow reference
      missing_subgraph  -- list of non-workflow model short_names missing the block
    """
    # Workflow canonical labels: class_code -> set of labels seen in workflow files
    workflow_nodes: Dict[str, Set[str]] = defaultdict(set)

    # Individual model labels: class_code -> {label -> set of short_names}
    model_nodes: Dict[str, Dict[str, Set[str]]] = defaultdict(lambda: defaultdict(set))

    missing_subgraph: List[str] = []

    for ma in analyses:
        sname = short_name(ma.model_file.path)
        is_wf = ma.model_file.is_workflow

        # Flag non-workflow formed models missing the subgraph
        if not is_wf and not ma.has_linked_entities_block:
            missing_subgraph.append(sname)

        # Collect nodes to index: linked entities + key entity
        nodes_to_index = list(ma.linked_entities)
        if ma.key_entity and ma.key_entity not in nodes_to_index:
            nodes_to_index.insert(0, ma.key_entity)

        for node_name in nodes_to_index:
            node = to_linked_node(node_name)
            if node is None:
                continue
            if is_wf:
                workflow_nodes[node.class_code].add(node.label)
            else:
                model_nodes[node.class_code][node.label].add(sname)

    # Workflow conflicts: per model, nodes that differ from workflow canonical label
    # Structure: {sname -> [{class_code, current_label, canonical_labels}]}
    workflow_conflicts: Dict[str, List[Dict]] = defaultdict(list)

    for code, label_map in model_nodes.items():
        wf_labels = workflow_nodes.get(code)
        if not wf_labels:
            continue
        for label, file_set in label_map.items():
            if label not in wf_labels:
                for sname in sorted(file_set):
                    workflow_conflicts[sname].append({
                        "class_code": code,
                        "current_label": label,
                        "canonical_labels": wf_labels,
                    })

    # Inter-model disagreements: class codes with >1 label, no workflow reference
    inter_model: List[Dict] = []
    for code, label_map in model_nodes.items():
        if code in workflow_nodes:
            continue  # covered by workflow conflicts
        if len(label_map) > 1:
            inter_model.append({
                "class_code": code,
                "labels": dict(label_map),
            })

    return {
        "workflow_conflicts": dict(workflow_conflicts),
        "inter_model_disagreements": inter_model,
        "missing_subgraph": missing_subgraph,
        "workflow_nodes": dict(workflow_nodes),
        "model_nodes": {k: dict(v) for k, v in model_nodes.items()},
    }


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def md_row(*cells: str) -> str:
    return "| " + " | ".join(str(c) for c in cells) + " |"


def generate_report(
    files: List[ModelFile],
    analyses: List[ModelAnalysis],
    result: Dict,
) -> str:
    lines: List[str] = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    individual = [f for f in files if not f.is_workflow]
    workflows = [f for f in files if f.is_workflow]

    lines += [
        "# Model Consistency Report",
        "",
        f"_Generated: {now}_",
        "",
        f"**Individual model files analysed:** {len(individual)}  ",
        f"**Workflow/overview files analysed:** {len(workflows)}  ",
        "",
        "This report checks consistency of inter-model linking nodes -- the entities "
        "declared in each model's `//subgraph Linked Entities` block and each model's "
        "key entity. High-multiplicity classes (E55 type terms, identifiers, images) "
        "are ignored unless explicitly declared as linked entities.",
        "",
        "---",
        "",
    ]

    # -----------------------------------------------------------------------
    # Section 1: Workflow conflicts (highest priority)
    # -----------------------------------------------------------------------
    conflicts = result["workflow_conflicts"]
    lines += [
        "## 1. Model update checklist (workflow conflicts)",
        "",
        "These models contain linked entity labels that differ from the canonical "
        "labels used in the workflow/overview TSV. Update the model to use the "
        "canonical label and increment its version number.",
        "",
    ]

    if not conflicts:
        lines.append(
            "_All linked entity labels are consistent with the workflow._\n"
        )
    else:
        total = sum(len(v) for v in conflicts.values())
        lines += [
            f"**Models requiring updates:** {len(conflicts)}  ",
            f"**Total label changes needed:** {total}  ",
            "",
        ]
        for sname in sorted(conflicts.keys()):
            changes = conflicts[sname]
            lines += [
                f"### `{sname}`",
                "",
                md_row("Class code", "Current label", "Change to"),
                md_row("---", "---", "---"),
            ]
            for c in sorted(changes, key=lambda x: x["class_code"]):
                canonical = " or ".join(
                    f"`{l}`" for l in sorted(c["canonical_labels"])
                )
                lines.append(md_row(
                    f"`{c['class_code']}`",
                    f"`{c['current_label']}`",
                    canonical,
                ))
            lines.append("")

    # -----------------------------------------------------------------------
    # Section 2: Inter-model disagreements (no workflow reference)
    # -----------------------------------------------------------------------
    inter = result["inter_model_disagreements"]
    lines += [
        "## 2. Inter-model disagreements (no workflow reference)",
        "",
        "These class codes appear as linked entities in more than one model with "
        "different labels, and are not covered by the workflow. Human decision "
        "needed: agree on a canonical label, then add it to the workflow and update "
        "the affected models.",
        "",
    ]

    if not inter:
        lines.append(
            "_No inter-model disagreements outside workflow coverage._\n"
        )
    else:
        for item in sorted(inter, key=lambda x: x["class_code"]):
            code = item["class_code"]
            lines += [
                f"### `{code}`",
                "",
                md_row("Label", "Used in"),
                md_row("---", "---"),
            ]
            for label, file_set in sorted(item["labels"].items()):
                lines.append(md_row(
                    f"`{label}`",
                    ", ".join(sorted(file_set)),
                ))
            lines.append("")

    # -----------------------------------------------------------------------
    # Section 3: Models missing Linked Entities subgraph
    # -----------------------------------------------------------------------
    missing = result["missing_subgraph"]
    lines += [
        "## 3. Models missing Linked Entities subgraph",
        "",
        "These formed model files do not contain a `//subgraph Linked Entities` "
        "block. Their linking nodes cannot be checked for consistency until the "
        "block is added.",
        "",
    ]

    if not missing:
        lines.append(
            "_All individual models have a Linked Entities subgraph._\n"
        )
    else:
        for sname in sorted(missing):
            lines.append(f"- `{sname}`")
        lines.append("")

    # -----------------------------------------------------------------------
    # Section 4: Verified shared nodes (informational)
    # -----------------------------------------------------------------------
    wf_nodes = result["workflow_nodes"]
    model_nodes = result["model_nodes"]

    # Nodes consistent with workflow across at least one individual model
    verified: List[Tuple[str, str, Set[str]]] = []
    for code, wf_labels in wf_nodes.items():
        label_map = model_nodes.get(code, {})
        for label in wf_labels:
            if label in label_map:
                verified.append((code, label, label_map[label]))

    lines += [
        "## 4. Verified shared nodes",
        "",
        "Linked entity nodes that are consistent between the workflow and at least "
        "one individual model. These are the confirmed inter-model join points.",
        "",
        md_row("Class code", "Canonical label", "Consistent in"),
        md_row("---", "---", "---"),
    ]

    if not verified:
        lines.append("_No verified shared nodes yet._")
    else:
        for code, label, file_set in sorted(verified, key=lambda x: x[0]):
            lines.append(md_row(
                f"`{code}`",
                f"`{label}`",
                ", ".join(sorted(file_set)),
            ))
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    files = discover_model_files()
    if not files:
        print("No TSV files found. Exiting.")
        sys.exit(0)

    individual = [f for f in files if not f.is_workflow]
    workflows = [f for f in files if f.is_workflow]
    print(
        f"Found {len(individual)} individual model(s) and "
        f"{len(workflows)} workflow file(s). Analysing..."
    )

    analyses = [parse_model_file(f) for f in files]
    result = analyse(analyses)

    report = generate_report(files, analyses, result)

    REPORTS_DIR.mkdir(exist_ok=True)
    REPORT_FILE.write_text(report, encoding="utf-8")
    print(f"Report written to {REPORT_FILE.relative_to(REPO_ROOT)}")

    n_conflicts = len(result["workflow_conflicts"])
    n_changes = sum(len(v) for v in result["workflow_conflicts"].values())
    n_inter = len(result["inter_model_disagreements"])
    n_missing = len(result["missing_subgraph"])
    print(f"  Workflow conflicts:           {n_conflicts} model(s), {n_changes} change(s)")
    print(f"  Inter-model disagreements:    {n_inter}")
    print(f"  Missing subgraph:             {n_missing}")


if __name__ == "__main__":
    main()
