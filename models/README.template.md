# HPSWG Models

This folder contains the semantic data models developed by the Heritage and Paintings Science Working Group (HPSWG) at the National Gallery, London. Models are expressed as tab-separated triple files (TSV) aligned to CIDOC CRM and related extension ontologies, and are designed for use with the [National Gallery Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/).

## How this folder is organised

Each subfolder represents either a workflow overview or a domain model:

- **Semantic workflow overviews** -- CIDOC CRM-aligned files showing inter-model connectivity. These serve as the canonical reference for shared node labels and are used by the automated consistency checker.
- **User workflow overviews** -- simplified overviews designed to help stakeholders agree on top-level connections before full semantic modelling begins. Not part of the consistency check.
- **Domain models** (`.tsv` files) -- fully mapped CIDOC CRM triples for a specific aspect of heritage science documentation, ready for visualisation in the Dynamic Modeller.
- **Precursor files** (`.txt` files) -- field mapping tables and draft notes representing domain models in early development.
- **Planned folders** -- reserved for future work, currently empty.

## Ontologies in use

<!-- BEGIN AUTO: ONTOLOGY-REF -->
_Ontology reference will be generated here._
<!-- END AUTO: ONTOLOGY-REF -->

## Model index

<!-- BEGIN AUTO: MODEL-FOLDERS -->
_Model folder index will be generated here._
<!-- END AUTO: MODEL-FOLDERS -->

## Additional information

### Folder structure

```
models/
  workflows/              # Semantic workflow overviews (canonical reference)
  user_workflows/         # User-facing simplified overviews
  <model_name>/           # Domain model folders
    <model_name>_vA.B.tsv
    README.md
```

### Creating or updating a model

1. Add a new folder inside `models/`.
2. Add a TSV file using the pattern `<model>_v0.1.tsv`.
3. Commit and push; the GitHub Action will:
   - Create or update that model's README
   - Update the top-level README
   - Integrate the model into the master list
   - Run the consistency checker and update `reports/consistency_report.md`
4. A TXT file using the pattern `<model>_notes.txt` can be added to record initial thoughts on a model before it has been fully formed.

---

If you would like help constructing new models or integrating them with CIDOC CRM, please open an issue or contact the maintainers.
