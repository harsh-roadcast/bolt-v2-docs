## System and Data Requirements

### Non-functional requirements

TripHub implementation must account for the following non-functional requirements:

- Route, trip, target and haltpoint list views must support pagination, search and filters without blocking interaction on large datasets.
- Map views must handle high marker counts through clustering, lazy loading or viewport-based rendering.
- Route rendering must fail gracefully when path geometry or map-service response is unavailable.
- Auto-routing generation must expose progress, timeout and retry states rather than leaving the user in a blocking loader.
- Mobile updates for target completion, POD, OTP, checklist, adhoc, SOS and breakdown events must be idempotent so repeated sync does not create duplicate events.
- Offline mobile actions should queue TripHub-facing events with local timestamp, device timestamp, sync status and retry state where offline mode is supported.
- Proof media must be uploaded securely and associated with trip, haltpoint, target/service request, user and timestamp context.
- PII related to students, employees, customers, phone numbers, OTP and POD must be permission-gated and masked where required.
- Audit logs must retain sensitive operational events such as route edits, target/haltpoint deletion, trip hold, trip completion, SOS, breakdown, adhoc approval and reassignment.
- Timezone display must be consistent across web, mobile and reports. Scheduler-owned recurrence timezone logic remains outside TripHub, but TripHub must display generated trip times correctly.
- Core flows should meet accessibility requirements for keyboard access, focus state, form labels, error states and colour contrast.
- Failure recovery must provide retry or actionable fallback for map errors, sync failure, proof upload failure, OTP failure, auto-routing timeout and stale assignment.

### Entity data

The system must maintain stable IDs for:

- Territory.
- Target.
- Haltpoint.
- Route.
- Trip.
- Scheduler reference IDs for shift/schedule where applicable.
- Route version.
- Vehicle.
- Driver/workforce.
- Adhoc request.
- Checklist response.
- Attendance record.
- SOS event.
- Breakdown event.
- Trip completion metadata, including normal completion versus early End Trip, missed haltpoints and incomplete target/service-request records.

### Route and trip versioning

Routes should be versioned when changes affect execution logic.

Version-creating changes include:

- Adding haltpoints.
- Removing haltpoints.
- Reordering haltpoints or changing sequence.
- Changing start point or end point.
- Changing route geometry/path.
- Changing service area.
- Changing linked territory.
- Changing route type.
- Changing auto-routing configuration that affects generated output.
- Changing service behavior, proof/checklist/completion configuration inherited from Route Type configuration.

Non-version changes include:

- Route name.
- Route description.
- Internal notes.
- Display-only metadata.

Trip/version behavior:

- Already-generated future trips update based on the latest route update until the trip is started.
- Started, in-progress, completed, cancelled or breakdown trips must retain the route version/snapshot used at execution start.
- Editing a route must not mutate completed or in-progress trip history.
- Re-run trips should create new trip records.

### Spatial data

The system must support:

- Latitude/longitude for targets and haltpoints.
- Service area geometry.
- Geofence linkage.
- KML upload and parsing where available.
- Map path and route path data.
- Address reverse-geocode where available.

### Audit data

Audit log must capture:

- Actor.
- Role.
- Entity ID.
- Action.
- Old value/new value where applicable.
- Timestamp.
- Organisation.
- Source device/app.

### Admin configuration data requirements

TripHub Admin Configuration requires the following backend objects:

- `triphub_target_setup` for organisation-to-target-type enablement.
- `triphub_target_attribute_schema` for target attribute sets by organisation and target type.
- `triphub_target_attribute_field` for field definitions, ordering, labels, type, validation, mandatory state, tooltip and helper text.
- `triphub_target_attribute_option` for dropdown and multiple-choice values.
- `triphub_route_type_config` for route type name, description, organisation link, active/archive state and route behavior rules.
- `triphub_route_type_service_type` for pickup/drop/exchange or future service-type mapping.
- Configuration audit log for create, edit, disable, archive, publish and migration actions.

Historical trip, route and target records must store enough snapshot data to remain readable even after an admin changes a target attribute schema or route type configuration.

### Scheduler integration data touchpoints

Because Scheduler and Shift Master will be maintained as a separate module, TripHub should only store or consume the minimum scheduler references required for route and trip visibility.

TripHub should support the following scheduler-linked references:

- `scheduler_shift_id` and display name, where a route or generated trip is linked to a shift.
- `scheduler_schedule_id`, where a route is linked to a scheduler-owned recurrence.
- `route_version_id` used by Scheduler at the time a trip is generated.
- `scheduled_trip_source = scheduler` for trips created through recurrence.
- `scheduler_status` for route-level display, such as scheduled, unscheduled, paused or error.
- `next_scheduled_generation_at` and `last_scheduler_sync_at`, if returned by Scheduler.
- `scheduler_error_summary`, where Scheduler fails to generate or sync a trip and TripHub needs to show a non-blocking operational warning.

TripHub must not own the recurrence rule schema, holiday calendar, exception model, generation-run engine, or Shift Master lifecycle. Those belong to the connected Scheduler specification.

### Mobile execution data requirements

Mobile execution requires additional event/snapshot storage:

- OTP attempts and verification result.
- POD photo/signature/notes metadata.
- Mobile cancellation reason and optional details.
- Mobile adhoc site photo and nearby-target match result.
- Breakdown can-move/cannot-move value.
- Replacement vehicle, replacement driver, ETA and number-plate scan result.
- SOS acknowledgement, call status and connected duration.
- Break policy, quota, countdown and overrun status.
- Forms Centre submissions and confirmation state.
- Offline queue, sync failure and stale-assignment resolution status.

---
