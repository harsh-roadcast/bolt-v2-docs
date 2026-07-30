## Acceptance Criteria

### General

- User can navigate to TripHub and access allowed sections based on permissions.
- List views support search, filters, pagination and row actions consistently.
- Data is scoped to organisation hierarchy.
- User actions are audit logged.

### Targets

- User can create, edit, disable and delete targets based on permission.
- Target list supports route-type-specific labels and columns.
- Target location is validated before route use.
- Target permanent delete requires confirmation and dependency-impact visibility.
- Target Frequency greater than 1 generates repeated service requests without creating duplicate target master records.
- Published target attributes can be hidden/disabled but not permanently deleted if data exists.

### Haltpoints

- User can create haltpoints and link targets.
- Haltpoints show linked target count and area/location details.
- Haltpoint edit respects route dependency rules.

### Territories

- User can create and edit territories/sub-territories.
- Territory linked-route count updates correctly.
- A route can belong to only one territory at a time.

### Routes

- User can create manual route through step-based workflow.
- User can create auto route where backend supports it.
- User can define or select service area.
- Service area mismatch with haltpoints is validated.
- Route review screen shows haltpoint count, service request count, service type, load, distance and time estimate.
- Route can be scheduled or flagged as not scheduled.
- Route edit allows haltpoint reordering where permitted but blocks direct target-set mutation unless a new route/versioning flow is used.
- Exchange service captures pickup and drop-side handling where required.

### Trips

- User can create trip from route and assign vehicle/driver.
- Trip list shows status, progress, target counts and timing fields.
- Trip detail panel shows Overview, Trip Path, Linked Data and Command Log.
- Trip statuses update correctly across Unassigned/Not Assigned, Assigned, Scheduled, In Progress, On Hold, Breakdown, Completed and Cancelled.
- Draft is not shown as a status unless a save-as-draft workflow is explicitly added.


### Workforce mobile execution

- Driver can see assigned trips in Ongoing, Upcoming and History tabs.
- Upcoming scheduled trips expose Start Trip where allowed.
- Mandatory pre-trip checklist blocks Start Trip until required items are complete.
- In-progress trip detail shows route timeline with haltpoints/targets and execution states.
- Driver can mark target states such as Picked, No Show, Missed, Pending or Completed based on route type.
- Mandatory proof capture blocks target completion until proof is submitted.
- Complete Trip warns the driver when targets remain incomplete.
- Put On Hold, SOS, Report Vehicle Breakdown and Call Admin create auditable events.
- Mobile adhoc request can be submitted using current coordinates/manual details without permanently mutating the master route by default.
- Approved adhoc requests can be assigned to ongoing, scheduled/upcoming or unassigned trips based on permission and route-type rules.

### Execution exceptions

- Breakdown creates event and updates trip status.
- Reassignment after breakdown shows Resume Trip to new driver.
- SOS creates event, notification and audit record.
- Adhoc requests can be assigned without mutating the master route.
- Hold, End and Re-run actions require reason and audit trail.
- Uncompleted targets from Load Full, Breakdown or Skipped Target scenarios can be reassigned to another active/upcoming/unassigned trip where permitted.
- Re-run creates a new trip instance from the original route configuration and excludes prior adhoc tasks by default.

### Map and replay

- Path replay opens for trips with route/path data.
- No-data state appears when no trip path exists.
- Map info card displays route/trip/haltpoint/target context.
- Route deviation alerts are generated and logged when route geofence monitoring is enabled and the vehicle moves outside allowed route/service-area thresholds.

### Admin configuration acceptance criteria

- Admin users with permission can access TripHub Configurations from Admin navigation.
- Admin users can view Target Setup, Target Attributes and Route Types configuration areas.
- Target Attributes list shows Organisation, Target Type, Last Updated On and Actions.
- Admin users can create/edit a target attribute schema with supported field types: Single Line, Paragraph, Multiple Choice, Drop Down, URL, Number, Date, File Upload and Currency.
- Field properties support label, placeholder, mandatory flag, validation, tooltip, helper text and options where applicable.
- Preview shows the configured target form and clearly communicates that it is a preview only.
- Route Type list shows Route Type, Last Updated On and Actions.
- Admin users can create/edit route type rules for Haltpoint Selection, Geofence Based Service Area, Service Type and Vehicle Assignment Allowed.
- Route Type configuration controls the route creation flow shown to operational users.
- Configuration changes are audit logged and do not corrupt historical TripHub records.
- Target Type is locked after TripHub add-on purchase/activation unless a migration workflow is approved.


### Additional acceptance criteria

Scheduler integration:

- Route List shows shift values, multiple shifts or `--` for unscheduled routes where Scheduler integration is enabled.
- Clicking a shift opens schedule information or deep-links to the Scheduler module.
- Scheduled route banner shows schedule/shift summary and Edit Schedule.
- Unscheduled route banner shows Schedule Route.
- Create Shift & Schedule opens Scheduler / Shift Master in a new tab or separate module context.
- Trips generated by Scheduler appear in TripHub Trip List with the correct route, route version, shift and scheduled time.
- Route edit/disable/versioning requests schedule-impact validation from Scheduler before applying changes that affect future trips.

Auto Routing:

- Auto-routing form captures vehicle categories, start/end point, average duration, average distance, average speed, sweep radius, vehicle count by category, capacity, maximum range where retained, service hubs/landfills, number of zones and recommended zone count.
- Every auto-routing field has type, required status, default, unit, min/max, tooltip and validation rule.
- System shows loading, generation-in-progress, partial-success, no-feasible-route, retry and backend-timeout states.
- Generated routes show assigned/unassigned haltpoints and validation warnings before creation.

Route Modes and Manual Selection:

- Manual, Auto and Service Area route flows render different required/optional/unavailable steps based on route type.
- Auto Route does not show Service Area Setup when route copy says service area cannot be defined.
- Haltpoint selections persist across search, filter, pagination and list/map switching.
- Continue is disabled until at least one eligible haltpoint is selected.
- Select current page and select all filtered results are distinct actions.

Route Empty/Edit/Disable:

- Route empty states cover no targets/no haltpoints, targets only, haltpoints only, both created and ready-to-create-route states.
- Route editing distinguishes adding/removing haltpoints from adding targets into haltpoints.
- Started/active trips keep their route snapshot after route edits; already-generated future trips update based on the route update until started.
- Disabling a route blocks future manual trip creation and scheduling while ongoing/started trips remain unchanged.

Trip List and Creation:

- Trip List supports Trip → Haltpoint → Target expansion.
- Route and Shift filters are available when scheduler is enabled.
- Duplicate Trip performs driver/vehicle conflict checks.
- Create Trip for this Route opens trip creation with route preselected.
- Create Trip supports Use Route as Geofence, Optimise Route, route preview, Back to Route, Start Date and End Date where shown in design.

Territory, Target and Haltpoint:

- Territory expanded view shows sub-territories and assigned routes.
- Target import includes Upload via KML where enabled.
- Target user-visibility rules support all users versus selected users.
- Haltpoint filters include organisation, created date, route linkage, territory, geofence and Show Only Hub.
- Target and haltpoint permanent delete is supported with permission, confirmation and dependency-impact visibility.

Mobile:

- OTP verification covers wrong OTP, retry and retry-limit behavior.
- POD supports mandatory photo, optional signature and notes based on route type.
- Cancel Trip requires reason, optional details and confirmation.
- Adhoc starts with site-photo capture where configured and supports nearby-target matching.
- Breakdown captures can-move/cannot-move and handles replacement vehicle, ETA, plate scan, incorrect-plate error and resume rules.
- Breaks show mandatory/flexible policy, fixed windows, remaining quota, countdown and End Break.
- SOS is included in TripHub V1 as a trip-execution emergency event; internet-call states include sent, failed/retry, incoming/outgoing, connected, ended and failed states where supported by the connected calling system.
- Forms Centre shows list, available count, form details and confirmation.
- Mobile acceptance includes loading, offline, permission-denied, sync-failed and stale-assignment states.

---
