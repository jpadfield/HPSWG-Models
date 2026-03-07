# HPSWG Models

This folder contains the semantic data models developed by the Heritage and Paintings Science Working Group (HPSWG) at the National Gallery, London. Models are expressed as tab-separated triple files (TSV) aligned to CIDOC CRM and related extension ontologies, and are designed for use with the [National Gallery Dynamic Modeller](https://research.nationalgallery.org.uk/lab/modelling/).

## How this folder is organised

Each subfolder represents a model domain. A folder may contain:

- **Formed models** (`.tsv` files) -- fully mapped CIDOC CRM triples, ready for visualisation in the Dynamic Modeller
- **Precursor files** (`.txt` files) -- field mapping tables and draft notes representing models in early development
- **Planned folders** -- reserved for future work, currently empty

The top of this page also lists the NG-wide overview model, which visualises connections across all model domains.

## Ontologies in use

<!-- BEGIN AUTO: ONTOLOGY-REF -->
See [`ONTOLOGIES.md`](../ONTOLOGIES.md) for full version details, source links, and compatibility notes. Ontologies currently in use:

| Ontology | Version | Prefix |
|----------|---------|--------|
| [CIDOC CRM](https://cidoc-crm.org/html/cidoc_crm_v7.1.3.html) | 7.1.3 | `crm` |
| [CRMdig](https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v4.0.html) | 4.0 | `crmdig` |
| [CRMsci](https://cidoc-crm.org/crmsci/ModelVersion/crmsci-3.0) | 3.0 | `crmsci` |
| [ResearchSpace](https://github.com/researchspace/researchspace) | _see notes_ | `EX` |
<!-- END AUTO: ONTOLOGY-REF -->

## Model index

<!-- BEGIN AUTO: MODEL-FOLDERS -->
_Model folder index will be generated here._
<!-- END AUTO: MODEL-FOLDERS -->

## Additional Information
### Folder Structure
```
models/
  <model_name>/
    <model_name>_vA.B.tsv
    README.md
```

### Creating or Updating a Model

1. Add a new folder inside `models/`.
2. Add a TSV file using the pattern `<model>_v0.1.tsv`.
3. Commit and push; the GitHub Action will:
   - Create or update that model’s README  
   - Update the top-level README  
   - Integrate the model into the master list
4. A TXT file again using the pattern `<model>_v0.1.txt` can be added to present initial thoughts on a model before it have been fully formed.

---

If you would like help constructing new models or integrating them with CIDOC CRM, please open an
issue or contact the maintainers.
