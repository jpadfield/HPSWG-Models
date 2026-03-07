# Ontologies

This document records the semantic ontologies used across the HPSWG-Models repository, including the versions in use, canonical namespaces, and links to source documentation.

All models are expressed using **CIDOC CRM 7.1.3** as the core ontology. Extension ontologies (CRMdig, CRMsci) have been lightly adjusted for compatibility with this version -- see the notes below for details. ResearchSpace-specific terms are included pragmatically, with CRM-aligned alternatives planned for future documentation.

## Ontology reference

| Ontology | Version | Prefix | Namespace | Documentation | Download |
|----------|---------|--------|-----------|---------------|----------|
| [CIDOC CRM](https://cidoc-crm.org/html/cidoc_crm_v7.1.3.html) | 7.1.3 | `crm` | `http://www.cidoc-crm.org/cidoc-crm/` | [Link](https://cidoc-crm.org/html/cidoc_crm_v7.1.3.html) | [RDFS](https://cidoc-crm.org/rdfs/7.1.3/CIDOC_CRM_v7.1.3.rdfs) |
| [CRMdig](https://cidoc-crm.org/crmdig/) | 4.0 | `crmdig` | `http://www.ics.forth.gr/isl/CRMdig/` | [Link](https://cidoc-crm.org/crmdig/) | [RDFS](https://cidoc-crm.org/crmdig/lrmoo/CRMdig_v4.0.rdfs) |
| [CRMsci](https://cidoc-crm.org/crmsci/) | 3.0 | `crmsci` | `http://www.ics.forth.gr/isl/CRMsci/` | [Link](https://cidoc-crm.org/crmsci/) | [RDFS](https://cidoc-crm.org/crmsci/CRMsci_v3.0.rdfs) |
| [ResearchSpace](https://github.com/researchspace/researchspace) | _see notes_ | `rs` | `https://www.researchspace.org/resource/system/` | [Link](https://github.com/researchspace/researchspace) | -- |

## Compatibility notes

### CRMdig and CRMsci

Both CRMdig v4.0 and CRMsci v3.0 have been adjusted at a small number of points to ensure compatibility with CIDOC CRM 7.1.3. Where adjustments have been made, the relevant classes and properties remain semantically equivalent to the published versions. Full details of any deviations will be recorded here as the models mature.

### ResearchSpace terms

ResearchSpace classes and properties are used within the National Gallery's ResearchSpace deployment. These are not part of a published ontology standard. Work is planned to document CRM-equivalent alternatives for each ResearchSpace term used, making the models portable beyond the ResearchSpace platform.

## Updating this file

This file is maintained manually. When ontology versions are updated, please update both this file and `scripts/ontologies.json`, which drives the short ontology reference tables generated automatically in each model README.
