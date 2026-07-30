## Adhoc Request Management

Adhoc requests represent unplanned work created during or around trip execution.

Creation sources:

- Driver.
- Supervisor.
- Admin.
- External system/API in future.

Assignment options:

- Assign to existing trip.
- Create new trip.
- Keep in pending queue.

![Assign an adhoc request](../.gitbook/assets/adhoc-assignment.png)

*The web assignment flow allows an authorised user to review unplanned work and attach it to an eligible trip.*

Rules:

- Adhoc requests may be created by driver, supervisor, admin or external system where enabled.
- Admin/supervisor approval should be required before adhoc work is assigned for execution unless an organisation explicitly enables auto-approval.
- Admin can approve or reject adhoc requests. Rejection must capture a reason.
- Approved adhoc requests can be assigned to ongoing, scheduled/upcoming or unassigned trips.
- Original master route remains unchanged.
- Adhoc requests affect the selected trip instance only.
- If an adhoc request is approved and assigned to a trip, it is appended to that trip execution only unless product defines a route-insertion workflow.
- Re-run excludes previous adhoc tasks unless explicitly configured to include them or the user adds them again.
- Adhoc completion must capture proof and timestamp using the same completion schema as planned targets.
- Adhoc assignment must record actor, time, reason, approval state and selected trip.
