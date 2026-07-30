## Trip Status Model

The confirmed TripHub workflows define the current status model. `Draft` is not part of the confirmed model and should not be treated as an active status unless a save-as-draft workflow is explicitly introduced later.

TripHub should support the following confirmed or design-supported trip statuses:

| Status | Meaning | User/system behavior |
|---|---|---|
| Unassigned / Not Assigned | Trip exists but required vehicle, driver or workforce assignment is missing. | Must be resolved before normal execution. Can be assigned by authorised web user. |
| Assigned | Trip has route/resource assignment but has not started. | Driver receives Start Trip where mobile execution exists. |
| Scheduled | Trip is planned for a future time window. | Appears under Upcoming in mobile where assigned. Can expose Start Trip / Cancel Trip based on timing and permission. |
| In Progress | Trip is actively being executed. | Live progress, route timeline and map state update. |
| On Hold | Trip is temporarily paused by driver/admin/system. | Execution is blocked or limited until resumed based on permission rules. |
| Breakdown | Driver or admin has marked a vehicle/workforce breakdown. | Exception event is created; reassignment and Resume Trip logic applies. |
| Completed | Trip is completed either through normal completion or through End Trip / early-ending flow. | Immutable except authorised correction/re-run flows. Missed or incomplete haltpoints/targets remain visible to admin through trip detail and reports. |
| Cancelled | Trip is cancelled before or during execution. | Requires reason and audit log. |

Status notes:

- `Draft` is removed from the confirmed model and should remain an open product decision only if save-as-draft trip creation is required.
- `Approved` appears in some design/table references, but it needs a product decision: it may represent route approval, trip approval or a scheduling state rather than runtime execution status.
- `Paused` should map to `On Hold` unless product chooses to support both as separate states.
- Breakdown and On Hold are separate statuses: breakdown events move the Trip status to `Breakdown`; manual/admin hold moves the Trip status to `On Hold`.

In Progress, Assigned or Not Assigned, Completed, On Hold, Cancelled, and hover states should be represented consistently across table chips, filters, map markers, and detail views.
