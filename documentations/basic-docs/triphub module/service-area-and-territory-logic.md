## Service Area and Territory Logic

TripHub must support service-area based operations independently from haltpoint-only route planning.

Supported cases:

### Case 1: Service-area-only route

The customer does not predefine haltpoints. A vehicle is assigned to a service area, and the driver performs adhoc or dynamic pickups inside that area. The route is area-based, not haltpoint-sequence based.

Rules:

- Service area becomes the operational boundary.
- Targets may be discovered, created or served dynamically based on configuration.
- Route completion may depend on manual end, time window, supervisor approval or configured service completion criteria.

### Case 2: Haltpoint route with service area

The user selects haltpoints and also assigns a service area.

Rules:

- If the service area is intended to restrict the route, all selected haltpoints must fall inside the service area unless product explicitly allows exceptions.
- If haltpoints fall outside the selected service area, the system should show a clear validation message.
- Product must define whether mismatch is a hard block or warning per route type.
- The service area should be visible during review.

### Case 3: Territory-linked service area

The user selects a territory, and available haltpoints/geofences are filtered to that territory.

Rules:

- Route should inherit territory context.
- Linked route count should update on territory record.
- Removing territory linkage should be blocked while active trips exist.
