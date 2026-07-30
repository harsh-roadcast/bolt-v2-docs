## Trip Execution

Bolt Workforce Mobile supports the driver-facing TripHub execution flows, while Bolt Web remains the supervisor and admin planning and monitoring surface.

Driver/field-agent actions:

- Start Trip.
- Resume Trip.
- Complete Trip.
- Mark target/haltpoint complete.
- Upload proof.
- Capture photo/signature where required.
- Create adhoc request.
- Trigger SOS.
- Trigger Breakdown.
- Start/End break.
- Complete checklist where required.

Execution rules:

- Start Trip should be available only to assigned workforce and valid trips.
- Resume Trip should appear instead of Start Trip when a trip has been reassigned after breakdown or pause.
- Target completion must record timestamp, coordinates, user, proof state and offline-sync status where applicable.
- Adhoc additions must not permanently mutate the master route unless explicitly saved as target/haltpoint through a configured workflow.
- Completed service actions are immutable by default. Targets already Picked, Dropped, Exchanged, Missed or Completed cannot be reordered or have their service type changed.
- Only targets/service requests that are En Route, Pending, Scheduled or Not Started may be eligible for reordering or service-type edits, subject to permissions and route-type rules.
- All runtime sequence changes must be logged against the trip instance and must not silently rewrite the master route.

---
