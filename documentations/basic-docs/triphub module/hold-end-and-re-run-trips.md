## Hold, End and Re-run Trips

TripHub must support supervisor/admin recovery actions when execution changes.

### Hold Trip

Hold pauses a trip without marking it complete or cancelled.

![Hold a trip](../.gitbook/assets/trip-hold-action.png)

*Holding a trip requires an explicit confirmation and preserves the trip for later resumption.*

Rules:

- Requires reason.
- Status becomes On Hold.
- Workforce should not be able to continue execution unless trip is resumed.
- Hold event appears in audit log.

### End Trip

End Trip force-stops execution and still results in the `Completed` trip status. TripHub should distinguish early ending through completion metadata and missed-haltpoint/target records, not through a separate `Ended` status.

Rules:

- Requires confirmation and reason.
- Changes trip status to Completed.
- Records incomplete and missed haltpoints/targets.
- Admin must have visibility into missed haltpoints and incomplete targets even if the driver ends the trip early.
- Prevents further execution unless re-run is created.

### Re-run Trip

Re-run creates a new executable instance from the original route or incomplete scope.

Rules:

- Re-run creates a new trip instance using the completed trip's original route, target/service-request set and route configuration.
- Re-run should not include previous adhoc requests by default.
- Vehicle and driver assignments may be updated before starting the re-run.
- Product may optionally allow users to re-run missed targets only, but the default should be full original route configuration.
- Must create a new trip ID.
- Original trip remains historically intact.
