## Admin-side TripHub Configuration

Admin-side TripHub Configuration is the control layer that allows authorised admin users to configure how TripHub behaves for each organisation, target type, and route type. The **TripHub Configurations** page contains three primary areas: **Target Setup**, **Target Attributes**, and **Route Types**.

This section should be treated as part of the TripHub product scope because these configurations directly affect web planning flows, route creation, target creation, mobile execution forms and reporting behavior.

![TripHub configuration landing page](../.gitbook/assets/admin-config-landing.png)

*The configuration landing page provides entry points for Target Setup, Target Attributes, and Route Types.*

### Configuration access and navigation

TripHub Configurations should be available from the Admin navigation for users with Super Admin or equivalent configuration permissions. It sits under the broader Admin area alongside other platform-level configuration modules.

The configuration landing page should show configuration cards for:

- **Target Setup** — assign TripHub target datasets/types to organisations.
- **Target Attributes** — create and manage custom target attributes for TripHub.
- **Route Types** — create and manage route type rules.

Rules:

- Non-admin users must not see or access TripHub configuration screens.
- Configuration changes must be organisation-scoped unless explicitly created as a global/default configuration.
- Every create, edit, disable or publish action must be audit logged.
- Configuration changes should not rewrite historical trips, historical target snapshots or completed execution records.

### Target Setup

Target Setup controls which target datasets or target types are enabled for an organisation.

![Target Setup list](../.gitbook/assets/admin-target-setup.png)

*Target Setup shows the target datasets currently available to each organisation.*

Target Setup should support:

- Selecting an organisation or organisation hierarchy.
- Enabling one or more TripHub target types/datasets for that organisation.
- Controlling whether the target type is visible in TripHub target lists, route creation and relevant reports.
- Preventing active route/trip breakage when a target type is removed or disabled.
- Showing clear empty, active and no-access states.

Expected target type examples:

- `Target_Bin`
- `Target_School`
- `Target_Trip`
- `Target_Employee`
- `Target_Customer`

Additional business rules from TripHub Solution Documentation:

- Target Setup is a one-time Admin-controlled setup layer per organisation.
- Target Setup assigns which organisation uses which target type, for example `Target_Bin` for waste-management operations.
- Target Type may be editable before the organisation purchases or activates the TripHub add-on.
- Once an organisation purchases or activates TripHub, the assigned Target Type must be locked because it controls terminology, target attributes, route planning, mobile execution and reports.
- Any post-activation target-type change must be treated as a migration request, not a normal edit action.

![Assign target type to an organisation](../.gitbook/assets/admin-assign-target.png)

*An admin selects the organisation and target type before confirming the assignment.*

### Target Attributes

Target Attributes allow admins to define dynamic fields for specific TripHub target types. These fields are then used by target creation/edit forms, preview forms, applicable mobile forms and reporting surfaces.

![Target Attributes list](../.gitbook/assets/admin-target-attributes.png)

*The attribute list is scoped by organisation and target type and exposes edit and preview actions.*

The Target Attributes list should show:

- Organisation
- Target Type
- Last Updated On
- Actions

The list should support:

- Create Attribute
- Filters
- Search / hierarchy filter where available
- Pagination
- Row-level actions such as Edit Attributes and Preview

Rules:

- Attribute sets must be scoped by organisation and target type.
- A target type may have only one active attribute schema per organisation unless versioning is introduced.
- Required fields must be enforced consistently across manual creation, CSV/import, API sync and mobile execution where applicable.
- Attribute labels should be user-facing, but system keys should remain stable once the field is published.
- Target Attributes cannot be permanently deleted once published or used. They may be hidden/disabled for future data entry, but historical values must remain available for existing targets, trips, reports and audit logs.
- Disabling or hiding a field must not remove historical values from completed trips, reports or audit logs.

### Target Attribute Builder

The Target Attribute Builder should allow admins to create and edit TripHub-specific dynamic fields.

![Add a target attribute field](../.gitbook/assets/admin-add-target-field.png)

*The field builder supports field type, label, placeholder, validation, tooltip, helper text, and mandatory-state controls.*

Builder structure:

- **Basic Info**
- Organisation Name
- Target Type
- Add Fields
- Edit Field Properties

Supported field types:

- Single Line
- Paragraph
- Multiple Choice
- Drop Down
- URL
- Number
- Date
- File Upload
- Currency

Field property controls:

- Field Type
- Label Name
- Placeholder Text
- Mandatory
- Validation / Enable
- Tooltip
- Helper Text
- Choices / Options for multiple-choice and dropdown fields
- Add Option for choice-based fields

Rules:

- Mandatory fields must block save when missing.
- Validation rules must run on create, edit, import and mobile submission surfaces.
- Tooltip and helper text should be shown wherever the field appears, provided the surface has room to display it.
- Dropdown and multiple-choice options must support add/remove before publish.
- Once data exists against a field, destructive changes should either be blocked or require migration rules.
- Field ordering in the builder should define display order in TripHub forms.

### Target Attribute Preview

Preview allows admins to verify the configured form before publishing or creating the attribute set. The preview is non-editable and exists only to show the form structure that TripHub users will receive.

![Target form preview](../.gitbook/assets/admin-target-form-preview.png)

*Preview reproduces the target form structure without creating operational target data.*

Preview should show:

- Target type specific form title, such as Bin Preview.
- Configured required fields and optional fields.
- Field labels, units, placeholder text and helper/tooltip affordances.
- Back and Create actions.

Example preview fields:

- ID
- Address
- Waste Type
- Latitude
- Longitude
- Load with Kg unit
- Owner
- Frequency

Rules:

- Preview must not create a target record.
- Preview must validate the form structure, not operational target data.
- Create from preview should create or publish the attribute schema, depending on final backend model.

### Route Types Configuration

Route Types Configuration allows admins to define how different route types behave during route creation and execution. It includes a Route Types list and a Create Route Type form.

The Route Types list should show:

- Route Type
- Last Updated On
- Actions

Route Type actions should include, at minimum:

- Create
- Edit
- Disable / Archive

The Create Route Type form should support:

- Route Type Name
- Description
- Link Organisation(s)
- Archived / active state where applicable
- Definition of how the route should be created
- Haltpoint Selection toggle
- Geofence Based Service Area toggle
- Service Type selection
- Vehicle Assignment Allowed toggle

Rules:

- Route Type Name is mandatory.
- Route Type rules should determine which route-creation steps appear to users.
- If **Haltpoint Selection** is disabled, the route builder should skip haltpoint selection and require an alternate execution structure such as service area/path.
- If **Geofence Based Service Area** is enabled, service area/path setup becomes available or required based on the route type configuration.
- Service Type should support one or more selected values such as Pickup, Drop and Exchange, unless a route type is configured as single-service only.
- If **Vehicle Assignment Allowed** is disabled, trip creation should not require or allow manual vehicle assignment for that route type.
- Disabling a route type should prevent new routes from using it but should not invalidate existing routes/trips.


### Extended Route Type configuration controls

The latest admin design and route-builder behavior require Route Type configuration to capture more than route name, organisation and service type. The following controls should be explicitly supported or marked as unavailable per release:

| Control | Expected behavior | Downstream impact |
|---|---|---|
| Driver Assignment Allowed | Enables or disables manual driver assignment during trip creation. | Controls trip creation validation, workforce assignment and mobile trip visibility. |
| Attendee Assignment Allowed | Enables helper/attendee assignment for route types that require crew, students, passengers or service attendants. | Controls attendee fields, attendance expectations and mobile/helper flows. |
| Vehicle Assignment Allowed | Enables or disables manual vehicle assignment. | Controls trip assignment and device/telemetry linkage. |
| Adhoc Request Enabled | Allows mobile/admin adhoc request creation for this route type. | Controls visibility of adhoc CTA, approval queue and trip-instance insertion. |
| Additional Adhoc Conditions | Defines whether adhoc requires approval, proof, target retention, nearby-target matching or service-type selection. | Controls mobile adhoc flow and admin review. |
| Service Request Completion Configuration | Defines what is required to complete pickup/drop/exchange/service tasks. | Controls OTP, POD, photo, notes, signature and completion validation. |
| Service Request Face Sync Configuration | Defines whether FaceSync verification is required before start, at haltpoint, at target or at completion. | Controls mobile blocking states and attendance/compliance logs. |
| Before Proof Mandatory | Requires proof before service starts. | Controls target-level execution flow. |
| After Proof Mandatory | Requires proof after service is completed. | Controls completion and POD validation. |
| Retain Created Adhoc Target | Determines whether mobile-created adhoc targets become permanent target master records after approval. | Controls master target table, reports and future planning. |

Configuration-change rules:

- Route Type changes must not rewrite completed trips or historical route versions.
- For active schedules, configuration changes should apply only to future generated trips unless the user explicitly edits current occurrences.
- If a Route Type setting is changed in a way that invalidates an existing route or schedule, the system must show impacted routes/schedules and require confirmation.
- If an existing route type disables a capability that current route versions depend on, historical route versions must remain readable and executable where already assigned.
- If Adhoc Request is disabled after adhoc work already exists, existing adhoc requests must remain visible in history and reports but no new adhoc requests should be created for future trips.

### Configuration impact matrix

| Configuration | Affects web planning | Affects mobile execution | Affects reports | Notes |
|---|---:|---:|---:|---|
| Target Setup | Yes | Indirectly | Yes | Controls which target types are available per organisation. |
| Target Attributes | Yes | Yes, where fields are used in execution/proof forms | Yes | Adds configurable columns/fields to target forms and reports. |
| Route Types | Yes | Yes | Yes | Controls route creation steps, service behavior and trip execution expectations. |
