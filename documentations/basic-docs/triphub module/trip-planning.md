## Trip Planning

A Trip is an executable instance of a route. Users should create a trip from a route or directly through Trip creation where route selection is part of the flow.

Trip creation should support:

- Route selection.
- Vehicle selection.
- Driver selection.
- Helper/attendee assignment where enabled.
- Start date/time and end date/time.
- Scheduler-derived schedule reference where applicable; recurrence configuration must happen in Scheduler / Shift Master, not inside TripHub trip creation.
- Visibility of tracking source: vehicle, device IMEI and last update timestamp.
- Validation of required fields before creation.
- Additional route type information such as Vehicle Category.


### Trip list metrics and deployed behavior

The live Trips page uses summary metrics above the trip table. The web experience should support metric cards for operational totals such as total trips, assigned or scheduled trips, active or in-progress trips, completed trips, on-hold or breakdown trips, and missed or pending work. Final metric names should follow the configured route type and entity label; for example, school transport may use Students while waste management may use Targets or Bins.

![Live trip monitoring](../.gitbook/assets/live-trip-monitoring.png)

*The deployed monitoring pattern combines summary metrics, table status, and a map preview for the selected operational context.*

Trip table behavior should support:

- Filter drawer and applied-filter state.
- Search by trip ID, route name, vehicle, driver, target/student and status where backend search supports it.
- Row action menu for edit, create trip from route, hold/end/re-run, path replay, call driver and operational commands where permission allows.
- Table-to-map transition without losing the selected row context.
- Export/download report where permission allows.

Trip list columns should include:

- ID
- Route Name
- Status
- Total Haltpoints
- Progress
- Total Targets or Total Students depending on route type
- Completed Targets/Students
- Missed Targets/Students
- Last Updated On
- Start Time
- End Time
- Actual Start Time
- Actual End Time
- Total Distance
- Total Time
- Vehicle
- Driver


### Trip list hierarchy and creation updates

The Trip List must support the expanded hierarchy shown in the updated designs.

![Expanded trip list](../.gitbook/assets/trip-list-expanded.png)

*The expanded trip table preserves trip-level status while exposing haltpoint and target or service-request rows.*

Hierarchy:

- Trip row.
- Haltpoint child rows.
- Target/service-request child rows.

Trip List requirements:

- Route and Shift filters must be available where scheduling is enabled.
- Expanded rows must show Trip → Haltpoint → Target relationship without losing trip-level status and progress context.
- Duplicate Trip action must create a new trip using the selected trip's reusable details, subject to conflict checks.
- Create Trip for this Route should open trip creation with the route preselected.
- Create & Schedule Route should behave as a navigation/deep-link action into Scheduler / Shift Master, not as recurrence configuration inside TripHub.

Create Trip fields and actions:

- Use Route as Geofence.
- Optimise Route.
- Route detail preview.
- Back to Route.
- Start Date.
- End Date.
- Route selection. Shift selection should appear only as a Scheduler-derived reference or deep-link, not as recurrence setup inside TripHub.
- Vehicle and driver assignment based on route type configuration.

![Create a trip](../.gitbook/assets/trip-create.png)

*Trip creation combines route context, time window, route/geofence rules, and assignment inputs.*

Duplicate Trip rules:

- Duplicated trips may copy route, route version, service requests, route type, proof requirements and configuration snapshot.
- Duplicated trips must not copy completed proof uploads, execution timestamps, SOS/breakdown events or historical adhoc completion data.
- Whether duplicated trips retain driver, vehicle, date and adhoc work requires explicit configuration/confirmation.
- System must check for overlapping driver and vehicle assignments before saving duplicated trips.
- Conflicts must show actionable copy: change driver, change vehicle, change time window or save as unassigned.
