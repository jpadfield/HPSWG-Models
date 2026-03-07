# Model Consistency Report

_Generated: 2026-03-07 18:27 UTC_

**Individual model files analysed:** 13  
**Workflow/overview files analysed:** 1  

This report checks consistency of inter-model linking nodes declared in each model's `//subgraph Linked Entities` block. Only declared linked entities are checked -- high-multiplicity classes such as E55 type terms are not flagged unless explicitly declared.

**Status key:**
- ✅ Consistent -- class codes match exactly
- 🔵 Hierarchy match -- related via CRM class hierarchy, confirm intent
- ⚠️ Class mismatch -- classes not related, check required
- ❓ Unknown target -- declared target folder not found in repo
- ⚠ No declaration -- `//links` directive missing, suggestions provided

---

## 1. Per-model link validation

Each model's linked entities are listed with their declared target models and consistency status. Where no `//links` declaration exists, possible targets are suggested based on matching class codes.

<details>
<summary><strong>heritage_object/heritage_object_v1.3.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |

</details>

<details>
<summary><strong>location/location_v1.0.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |

</details>

<details>
<summary><strong>person/person_v0.9.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |

</details>

<details>
<summary><strong>production_event/production_event_v1.0.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |

</details>

<details>
<summary><strong>project/project_v1.0.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |

</details>

<details>
<summary><strong>sample/sample_v1.6.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |

</details>

<details>
<summary><strong>sample_modification/sample_modification_v1.3.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |

</details>

<details>
<summary><strong>sample_site/sample_site_v1.4.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |

</details>

<details>
<summary><strong>sample_storage_unit/sample_storage_unit_v1.0.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |

</details>

<details>
<summary><strong>sample_taking_event/sample_taking_event_v1.4.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |

</details>

<details>
<summary><strong>sampling_event/sampling_event_v1.1.tsv</strong></summary>

| Linked entity | Class code | Declared target(s) | Status |
| --- | --- | --- | --- |

</details>

## 2. Models missing Linked Entities subgraph

These formed model files do not contain a `//subgraph Linked Entities` block. Add the block to enable consistency checking.

- `frame_part/frame_part_v1.0.tsv`
- `heritage_object_part/heritage_object_part_v1.0.tsv`
