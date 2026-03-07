# Model Consistency Report

_Generated: 2026-03-07 16:45 UTC_

**Individual model files analysed:** 13  
**Workflow/overview files analysed:** 1  

This report identifies potential inconsistencies in node naming across the HPSWG-Models TSV files. It is generated automatically on each push and is intended as a working tool for model authors, not a definitive quality assessment.

---

## 1. Model update checklist

Each entry below lists an individual model file that contains node labels which differ from the canonical labels used in the workflow/overview TSV. The workflow is treated as the reference. Update the model file to use the canonical label, then increment its version number.

**Models requiring updates:** 8  
**Total label changes needed:** 18  

### `heritage_object/heritage_object_v1.3.tsv`

| Class code | Current label | Change to |
| --- | --- | --- |
| `EX_Digital_Image` | `Object Image` | `Analytical Sample Image` or `Annotation Image` or `Sample Image` |

### `location/location_v1.0.tsv`

| Class code | Current label | Change to |
| --- | --- | --- |
| `E55` | `Identifier Type` | `IIIF selector point (image-space)` |
| `E94` | `Geometry (Space Primitive)` | `Sampling Point` |

### `person/person_v0.9.tsv`

| Class code | Current label | Change to |
| --- | --- | --- |
| `E55` | `Identifier Type` | `IIIF selector point (image-space)` |
| `E55` | `family-name` | `IIIF selector point (image-space)` |
| `E55` | `given-name` | `IIIF selector point (image-space)` |
| `E55` | `honorific-title` | `IIIF selector point (image-space)` |

### `project/project_v1.0.tsv`

| Class code | Current label | Change to |
| --- | --- | --- |
| `E55` | `condition state type` | `IIIF selector point (image-space)` |

### `sample/sample_v1.5.tsv`

| Class code | Current label | Change to |
| --- | --- | --- |
| `E22` | `Painting` | `Heritage Object` |
| `E53` | `Institution or Address` | `Storage Location` |
| `E55` | `condition state type` | `IIIF selector point (image-space)` |
| `E55` | `sample format` | `IIIF selector point (image-space)` |
| `E55` | `sample material type` | `IIIF selector point (image-space)` |

### `sample_site/sample_site_v1.4.tsv`

| Class code | Current label | Change to |
| --- | --- | --- |
| `E26` | `Area of Interest` | `Sample Site` |
| `EX_Digital_Image` | `Site Image` | `Analytical Sample Image` or `Annotation Image` or `Sample Image` |

### `sample_taking_event/sample_taking_event_v1.4.tsv`

| Class code | Current label | Change to |
| --- | --- | --- |
| `E55` | `condition state type` | `IIIF selector point (image-space)` |
| `S13` | `Sample` | `Material Sample` |

### `sampling_event/sampling_event_v1.1.tsv`

| Class code | Current label | Change to |
| --- | --- | --- |
| `E55` | `condition state type` | `IIIF selector point (image-space)` |

## 2. Predicate-scoped label variants across individual models

These cases show where the same CRM property connects nodes with the same class code but different labels in different individual models. Some of these will be intentional (an `E22` node genuinely represents different things in different models); others may be unintentional drift. Review each group to confirm intent.

| Property | Class code | Label | Files |
| --- | --- | --- | --- |
| `O3_sampled_from (1 to 1)` | `E22` | `Heritage Object` | sample_taking_event/sample_taking_event_v1.4.tsv |
|  |  | `Painting` | sample/sample_v1.5.tsv |
| `P1_is_identified_by (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Storage Unit` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P2_has_type (1 to n)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Storage Unit` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P46_is_composed_of (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Support` | heritage_object/heritage_object_v1.3.tsv |
| `P46i_forms_part_of (0 to 1)` | `E22` | `Heritage Object Part` | sample_site/sample_site_v1.4.tsv |
|  |  | `Storage Unit` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P48_has_preferred_identifier (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Storage Unit` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P50_has_current_keeper (1 to 1)` | `E22` | `Heritage Object` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Storage Unit` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P138i_has_representation (0 to n)` | `E26` | `Area of Interest` | sample_site/sample_site_v1.4.tsv |
|  |  | `Sample Site` | sample_site/sample_site_v1.4.tsv |
| `P89_falls_within (0 to n)` | `E26` | `Area of Interest` | sample_site/sample_site_v1.4.tsv |
|  |  | `Sample Site` | sample_site/sample_site_v1.4.tsv |
| `O16_observed_value (1 to 1)` | `E3` | `Condition state (Object Status)` | sampling_event/sampling_event_v1.1.tsv |
|  |  | `Condition state (Sample Site Status)` | sample_taking_event/sample_taking_event_v1.4.tsv |
| `P2_has_type (1 to 1)` | `E3` | `Condition state (Object Status)` | sampling_event/sampling_event_v1.1.tsv |
|  |  | `Condition state (Project Status)` | project/project_v1.0.tsv |
|  |  | `Condition state (Sample Site Status)` | sample_taking_event/sample_taking_event_v1.4.tsv |
|  |  | `Condition state (Sample Status)` | sample/sample_v1.5.tsv |
| `P44_has_condition (1 to n)` | `E3` | `Condition state (Project Status)` | project/project_v1.0.tsv |
|  |  | `Condition state (Sample Status)` | sample/sample_v1.5.tsv |
| `P45i_is incorporated in (0 to n)` | `E31` | `Location Documents` | location/location_v1.0.tsv |
|  |  | `Person Documents` | person/person_v0.9.tsv |
|  |  | `Production Documents` | production_event/production_event_v1.0.tsv |
|  |  | `Related Documents` | project/project_v1.0.tsv |
|  |  | `Report or Document` | heritage_object/heritage_object_v1.3.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Sample Documents` | sample/sample_v1.5.tsv |
|  |  | `Storage Documents` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P67i_is_referred_to_by (0 to n)` | `E31` | `Location Documents` | location/location_v1.0.tsv |
|  |  | `Production Documents` | production_event/production_event_v1.0.tsv |
| `P70i_is_documented_in (0 to n)` | `E31` | `Production Documents` | production_event/production_event_v1.0.tsv |
|  |  | `Related Documents` | project/project_v1.0.tsv |
|  |  | `Report or Document` | heritage_object/heritage_object_v1.3.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Sample Documents` | sample/sample_v1.5.tsv |
| `P2_has_type (1 to 1)` | `E35` | `Alternate Title` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Full Title` | heritage_object/heritage_object_v1.3.tsv |
| `P14_carried_out_by (1 to n)` | `E39` | `Group or Artist` | production_event/production_event_v1.0.tsv |
|  |  | `Institution or Person` | sample_modification/sample_modification_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `P50_has_current_keeper (1 to 1)` | `E39` | `Institution or Person` | heritage_object/heritage_object_v1.3.tsv, sample/sample_v1.5.tsv |
|  |  | `Storage Keeper` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P1_is_identified_by (0 to 1)` | `E41` | `Family Name` | person/person_v0.9.tsv |
|  |  | `Given Name` | person/person_v0.9.tsv |
|  |  | `Honorific / Title` | person/person_v0.9.tsv |
|  |  | `Unique System Label or ID` | heritage_object/heritage_object_v1.3.tsv |
| `P1_is_identified_by (1 to 1)` | `E41` | `Sample Site Name/Number` | sample_site/sample_site_v1.4.tsv |
|  |  | `Unique System Label` | location/location_v1.0.tsv, person/person_v0.9.tsv, production_event/production_event_v1.0.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
|  |  | `Unique System Label or ID` | project/project_v1.0.tsv, sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `P2_has_type (1 to 1)` | `E41` | `Family Name` | person/person_v0.9.tsv |
|  |  | `Given Name` | person/person_v0.9.tsv |
|  |  | `Honorific / Title` | person/person_v0.9.tsv |
| `P1_is_identified_by (0 to n)` | `E42` | `Alternative Identifier` | sample/sample_v1.5.tsv |
|  |  | `Alternative Identifiers` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `External Identifier` | person/person_v0.9.tsv |
|  |  | `External Place Identifier` | location/location_v1.0.tsv |
| `P2_has_type (1 to 1)` | `E42` | `Accession Number (custodian)` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `External Identifier` | person/person_v0.9.tsv |
|  |  | `External Place Identifier` | location/location_v1.0.tsv |
|  |  | `Persistent Identifier (PID)` | heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, production_event/production_event_v1.0.tsv, sample_modification/sample_modification_v1.3.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P48_has_preferred_identifier (1 to 1)` | `E42` | `Persistent Identifier (PID)` | heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, person/person_v0.9.tsv, production_event/production_event_v1.0.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
|  |  | `Persistent Identifier (UUID)` | sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Persistent Identifier (e.g. IGSN)` | sample/sample_v1.5.tsv |
| `P4_has_time-span (0 to 1)` | `E52` | `Birth Date` | person/person_v0.9.tsv |
|  |  | `Death Date` | person/person_v0.9.tsv |
| `P4_has_time-span (1 to 1)` | `E52` | `Activity Timespan` | person/person_v0.9.tsv |
|  |  | `Modification Date` | sample_modification/sample_modification_v1.3.tsv |
|  |  | `Production date` | production_event/production_event_v1.0.tsv |
|  |  | `Project Dates` | project/project_v1.0.tsv |
| `P54_has_current_permanent_location (1 to 1)` | `E53` | `Institution or Place` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Storage Location` | sample/sample_v1.5.tsv |
| `P7_took_place_at (1 to 1)` | `E53` | `Place of Modification` | sample_modification/sample_modification_v1.3.tsv |
|  |  | `Place of Production` | production_event/production_event_v1.0.tsv |
|  |  | `Sampling Location` | sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `P177_assigned_property_type` | `E55` | `sample attribute format` | sample_modification/sample_modification_v1.3.tsv |
|  |  | `sample attribute status` | sample_modification/sample_modification_v1.3.tsv |
| `P2_has_type (0 to 1)` | `E55` | `Geometry Type` | location/location_v1.0.tsv |
|  |  | `storage status` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P2_has_type (0 to n)` | `E55` | `Discipline` | person/person_v0.9.tsv |
|  |  | `sample keywords` | sample/sample_v1.5.tsv |
| `P2_has_type (1 to 1)` | `E55` | `Identifier Type` | location/location_v1.0.tsv, person/person_v0.9.tsv |
|  |  | `condition state type` | project/project_v1.0.tsv, sample/sample_v1.5.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `family-name` | person/person_v0.9.tsv |
|  |  | `given-name` | person/person_v0.9.tsv |
|  |  | `honorific-title` | person/person_v0.9.tsv |
|  |  | `sample format` | sample/sample_v1.5.tsv |
|  |  | `sample material type` | sample/sample_v1.5.tsv |
| `P2_has_type (1 to n)` | `E55` | `Project Type` | project/project_v1.0.tsv |
|  |  | `modification type` | sample_modification/sample_modification_v1.3.tsv |
|  |  | `object type` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `production type` | production_event/production_event_v1.0.tsv |
|  |  | `sample status` | sample_modification/sample_modification_v1.3.tsv |
|  |  | `storage type` | sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `P10_falls_within (0 to 1)` | `E7` | `Parent Project` | project/project_v1.0.tsv |
|  |  | `Project` | project/project_v1.0.tsv |
| `P1_is_identified_by (1 to 1)` | `E7` | `Project` | project/project_v1.0.tsv |
|  |  | `Sampling Event` | sampling_event/sampling_event_v1.1.tsv |
| `P4_has_time-span (1 to 1)` | `E7` | `Period of Activity` | person/person_v0.9.tsv |
|  |  | `Project` | project/project_v1.0.tsv |
| `P67i_is_referred_to_by (1 to 1)` | `E7` | `Project` | project/project_v1.0.tsv |
|  |  | `Sampling Event` | sampling_event/sampling_event_v1.1.tsv |
| `P70i_is_documented_in (0 to n)` | `E7` | `Project` | project/project_v1.0.tsv |
|  |  | `Sampling Event` | sampling_event/sampling_event_v1.1.tsv |
| `crm:P9i_forms_part_of` | `E7` | `Project` | sampling_event/sampling_event_v1.1.tsv |
|  |  | `Sampling Event` | sampling_event/sampling_event_v1.1.tsv |
| `P45i_is incorporated in (0 to n)` | `E73` | `Credit Line` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Description` | sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Description Text` | heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, person/person_v0.9.tsv, production_event/production_event_v1.0.tsv, sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.3.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
|  |  | `Physical Description` | sample_site/sample_site_v1.4.tsv |
|  |  | `Project Description` | project/project_v1.0.tsv |
|  |  | `Reason for Sampling` | sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Site Selection Comment` | sample_site/sample_site_v1.4.tsv |
|  |  | `Site Selection Description` | sample_site/sample_site_v1.4.tsv |
| `P67i_is_referred_to_by (0 to 1)` | `E73` | `Credit Line` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Site Selection Comment` | sample_site/sample_site_v1.4.tsv |
|  |  | `Site Selection Description` | sample_site/sample_site_v1.4.tsv |
| `P67i_is_referred_to_by (1 to 1)` | `E73` | `Description` | sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
|  |  | `Description Text` | heritage_object/heritage_object_v1.3.tsv, production_event/production_event_v1.0.tsv |
|  |  | `Physical Description` | sample_site/sample_site_v1.4.tsv |
|  |  | `Project Description` | project/project_v1.0.tsv |
| `P138i_has_representation (0 to n)` | `EX_Digital_Image` | `Object Image` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Sample Image` | sample/sample_v1.5.tsv |
|  |  | `Site Image` | sample_site/sample_site_v1.4.tsv |
| `PX_has_main_representation (0 to 1)` | `EX_Digital_Image` | `Main Object Image` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `Main Sample Image` | sample/sample_v1.5.tsv |
|  |  | `Main Site Image` | sample_site/sample_site_v1.4.tsv |
| `has legend` | `Properties` | `P46=is composed of (part–whole); P198=holds or supports (mechanical support between distinct objects); P56=bears feature (inseparable surface/embedded feature).` | frame_part/frame_part_v1.0.tsv |
|  |  | `P46=is composed of (part–whole); P198=holds or supports / P198i=is held or supported by (mechanical support between distinct objects); P56=bears feature (inseparable surface/embedded feature).` | heritage_object_part/heritage_object_part_v1.0.tsv |
| `P2_has_type (1 to 1)` | `aat` | `300312355` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `300387580` | heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, production_event/production_event_v1.0.tsv, sample_modification/sample_modification_v1.3.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
|  |  | `300417209` | heritage_object/heritage_object_v1.3.tsv |
|  |  | `300417227` | heritage_object/heritage_object_v1.3.tsv |

## 3. Shared nodes (exact name match across models)

Nodes that appear with exactly the same name in more than one model file. These are the current inter-model linking points. Consistency here is good; this section is informational.

| Node | Appears in |
| --- | --- |
| `Addition/Extension (integrated) (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Addition/Extension (separable) (E22)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `E11: Sample Modification` | sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.3.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `E16: Measurement` | sample/sample_v1.5.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `E22: Heritage Object` | heritage_object/heritage_object_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `E22: Painting` | production_event/production_event_v1.0.tsv, sample/sample_v1.5.tsv |
| `E26: Sample Site` | sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `E29: Method or Procedure` | sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E31: Report or Document` | heritage_object/heritage_object_v1.3.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E39: Institution or Person` | heritage_object/heritage_object_v1.3.tsv, sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.3.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E41: Unique System Label` | location/location_v1.0.tsv, person/person_v0.9.tsv, production_event/production_event_v1.0.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `E41: Unique System Label or ID` | heritage_object/heritage_object_v1.3.tsv, project/project_v1.0.tsv, sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E42: Persistent Identifier (PID)` | heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, person/person_v0.9.tsv, production_event/production_event_v1.0.tsv, project/project_v1.0.tsv, sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `E42: Persistent Identifier (UUID)` | sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E52: Sampling Date` | sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E53: Sampling Location` | sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E53: Storage Location` | sample/sample_v1.5.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `E55: Identifier Type` | location/location_v1.0.tsv, person/person_v0.9.tsv |
| `E55: condition state type` | project/project_v1.0.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E55: sample format` | sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.3.tsv |
| `E73: Description` | sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E73: Description Text` | heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, person/person_v0.9.tsv, production_event/production_event_v1.0.tsv, sample/sample_v1.5.tsv, sample_modification/sample_modification_v1.3.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |
| `E73: Reason for Sampling` | sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `E7: Project` | project/project_v1.0.tsv, sampling_event/sampling_event_v1.1.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `E7: Sampling Event` | sampling_event/sampling_event_v1.1.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `EX_Digital_Image: Sample Image` | sample/sample_v1.5.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `EX_Digital_Image_Region` | sample_site/sample_site_v1.4.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `Fixtures/Fittings/Hardware (E22)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Formats: object=E22 Human-Made Object; object_bn=S20 Rigid Physical Feature (linked with P46); place_bn=S20 Rigid Physical Feature (linked with P56); idea_bn=to review/interpretive.` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Gilding Layer (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Ground/Preparation (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Ground/Preparation Layer (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Inscriptions/Numbers (painted/incised) (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Label/Seal (attached object) (E22)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Painting (E22)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Repairs/Mends to Support (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Restoration Additions (general) (E22)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Restoration Retouch/Reconstruction (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `S13: Sample` | sample_modification/sample_modification_v1.3.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.4.tsv |
| `S24: Sample Splitting` | sample/sample_v1.5.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `S27: Observation` | sample/sample_v1.5.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `S2: Sample Taking` | sample/sample_v1.5.tsv, sample_site/sample_site_v1.4.tsv, sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv, workflows/workflow_cidoc_sample_taking_v1.0.tsv |
| `S4: Observation` | sample_taking_event/sample_taking_event_v1.4.tsv, sampling_event/sampling_event_v1.1.tsv |
| `Sample Sites/Voids (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Surface Coatings (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Surface Dirt/Accretion/Efflorescence (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `Varnish Layer (S20)` | frame_part/frame_part_v1.0.tsv, heritage_object_part/heritage_object_part_v1.0.tsv |
| `aat:300387580` | heritage_object/heritage_object_v1.3.tsv, location/location_v1.0.tsv, production_event/production_event_v1.0.tsv, sample_modification/sample_modification_v1.3.tsv, sample_storage_unit/sample_storage_unit_v1.0.tsv |

## 4. Files analysed

| File | Type |
| --- | --- |
| `frame_part/frame_part_v1.0.tsv` | Individual model |
| `heritage_object/heritage_object_v1.3.tsv` | Individual model |
| `heritage_object_part/heritage_object_part_v1.0.tsv` | Individual model |
| `location/location_v1.0.tsv` | Individual model |
| `person/person_v0.9.tsv` | Individual model |
| `production_event/production_event_v1.0.tsv` | Individual model |
| `project/project_v1.0.tsv` | Individual model |
| `sample/sample_v1.5.tsv` | Individual model |
| `sample_modification/sample_modification_v1.3.tsv` | Individual model |
| `sample_site/sample_site_v1.4.tsv` | Individual model |
| `sample_storage_unit/sample_storage_unit_v1.0.tsv` | Individual model |
| `sample_taking_event/sample_taking_event_v1.4.tsv` | Individual model |
| `sampling_event/sampling_event_v1.1.tsv` | Individual model |
| `workflows/workflow_cidoc_sample_taking_v1.0.tsv` | Workflow/overview |
