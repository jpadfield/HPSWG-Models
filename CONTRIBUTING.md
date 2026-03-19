# Contributing to HPSWG-Models

This document describes the conventions and formats used in this repository. It is intended for anyone adding new models, editing existing models, or extending the supporting scripts.

---

## TSV model format

Each model is a tab-separated file where each line is a triple:

```
Subject	Predicate	Object	Format
```

The format column uses `|` to separate the subject format class (left) and object format class (right). Format classes only need to be declared on the first mention of a node. See the [project state document](docs/) for the full list of format classes and TSV conventions.

---

## Directive lines

Lines beginning with `//` are directives. They are not rendered as triples in the diagram but may be read by the Dynamic Modeller or the repository scripts.

| Directive | Purpose |
|---|---|
| `//flowchart LR` | Sets top-level flow direction |
| `//subgraph TITLE` | Opens a subgraph block |
| `//end` | Closes a subgraph block |
| `//links NODE --> target` | Declares inter-model links for consistency checking |
| `//field ...` | Declares a field for table generation (see below) |
| `//field-via ...` | Declares a navigated field for table generation (see below) |
| `// any text` | Comment, ignored by all tools |

---

## Inter-model links

The `//links` directive is used by the consistency checker to verify that linked entities in a model match their canonical counterparts in other models. See the [consistency report](reports/) for current status.

```
//links E39: Project Owner --> person, organisation [confirmed]
```

The `[confirmed]` flag indicates that a subclass or superclass relationship is intentional.

---

## Field directives

`//field` and `//field-via` directives are used to generate human-readable field tables for form and data input design. Generated tables are collected in the [forms](forms/) folder. All field directives should be placed at the bottom of the model file, after all structural triples.

### `//field`

Use for fields that are present as nodes in the model.

```
//field NODE | ORDER | ALTERNATIVES | OPTIONAL NOTE
```

| Part | Description |
|---|---|
| `NODE` | The node label as it appears in the model, e.g. `E42: Persistent Identifier (PID)` |
| `ORDER` | Integer controlling the row order in the generated table |
| `ALTERNATIVES` | Semicolon-separated list of alternative labels, e.g. `Project ID; PID` |
| `OPTIONAL NOTE` | Additional contextual note appended in brackets to the label description in the table. Omit if not needed. |

The human-readable label is derived by stripping the CRM prefix from the node label. The label description is taken from the node's `tooltip` line in the model. The required status is derived from the multiplicity lower bound in the predicate connecting the node to its parent. Alternative labels that duplicate the human label are silently removed.

Example:

```
//field E42: Persistent Identifier (PID) | 1 | Project ID; PID
//field E7: Parent Project | 9 | Programme; Umbrella Project | Could be mapped as E89 Propositional Object but ResearchSpace implements it as E7 Activity.
```

### `//field-via`

Use for fields that are not present as nodes in the model but are practically needed in a form or display context, reachable by navigating through a related entity.

```
//field-via TARGET via INTERMEDIATE | ORDER | ALTERNATIVES | DESCRIPTION | OPTIONAL NOTE
```

| Part | Description |
|---|---|
| `TARGET` | The node carrying the value, e.g. `E39: Artist` |
| `INTERMEDIATE` | The node present in the model through which the target is reached, e.g. `E12: Production` |
| `ORDER` | Integer controlling the row order in the generated table |
| `ALTERNATIVES` | Semicolon-separated list of alternative labels |
| `DESCRIPTION` | Required label description, since there is no tooltip to draw from |
| `OPTIONAL NOTE` | Additional contextual note appended in brackets after the description. Omit if not needed. |

The CRM Code column in the generated table displays the navigation path, e.g. `E12 > E39`. The human-readable label is derived by stripping the CRM prefix from the target node label. Alternative labels that duplicate the human label are silently removed.

Example:

```
//field-via E39: Artist via E12: Production | 3 | Creator of heritage object; Artist; Creator | The actor who carried out the production.
```

### Delimiter note

Field directives use `|` as the column separator and `;` as the separator within the alternatives list. Do not use commas to separate alternative labels -- the Dynamic Modeller normalises comma-separated values to tabs during processing, which will corrupt the directive.

---

## Tooltips and label descriptions

The `tooltip` predicate adds hover text to a node in the Dynamic Modeller diagram. For nodes included via `//field` directives, the tooltip text is also used as the label description in the generated field table. Tooltips should therefore serve both purposes: concise enough for a diagram tooltip, complete enough to describe the field to a data entry user.

Where tooltip text and the intended label description have drifted apart, the tooltip should be updated to match. The TSV model is the single source of truth -- the generated field tables are derived output.

---

## Node labels and human-readable labels

The human-readable label displayed in the generated field table is derived directly from the node label by stripping the CRM class prefix (e.g. `E42: ` is stripped to give `Persistent Identifier (PID)`). Node labels should therefore be written with this in mind. Where a node label does not yet read well as a plain-language label, this should be noted and addressed when the model is next revised, rather than compensating with an alternative label in the `//field` directive.

---

## Adding a new model

1. Create a new folder under `models/` named after the model domain.
2. Add the TSV file named `<model_name>_v0.1.tsv`.
3. Add a `README.md` -- this will be overwritten by the auto-generator on the next push, but an empty file is needed to initialise the folder.
4. Add `//links` directives for any linked entities and check the consistency report after pushing.
5. Add `//field` and `//field-via` directives at the bottom of the TSV if the model is ready for field table generation.

---

## Scripts

| Script | Purpose |
|---|---|
| `scripts/update_readmes.py` | Generates all README files and field tables; run by GitHub Actions on push |
| `scripts/check_consistency.py` | Checks inter-model consistency via `//links` directives; run by GitHub Actions on push |
| `scripts/ontologies.json` | Ontology version config; maintain manually when versions change |
| `scripts/crm_hierarchy.json` | CRM class hierarchy used by the consistency checker; maintain manually |

---

## Questions and issues

For questions about the models or scripts, open an issue in the repository or contact the maintainers at the National Gallery, London.
