## Path Replay and TripHub Map

TripHub should provide a map-based route/trip review experience.

Path Replay should support:

- Playback of executed trip path.
- Route path display.
- Haltpoint and target markers.
- Completed/missed states.
- Previous/Next controls.
- Timeline or sequence list where supported.
- Linked Data and Command Log access.
- No-data state when trip has no path data.

![Trip path replay](../.gitbook/assets/trip-path-replay.png)

*Path Replay presents the executed path, status context, controls, and trip information together.*

TripHub Map should support:

- Route-level and trip-level spatial view.
- Entity info card for trip, route, target or haltpoint.
- Overview tab.
- Route Path / Trip Path tab.
- Linked Data tab.
- Command Log tab.
- Map markers for haltpoints and targets.
- Context-preserving navigation from list to map and back.

![TripHub map overview](../.gitbook/assets/triphub-map-overview.png)

*The map overview supports operational filters and status-based visibility for active and historical entities.*

![TripHub map target context](../.gitbook/assets/triphub-map-targets.png)

*Target and haltpoint views preserve spatial context while exposing the related entity information.*

### Route geofence and deviation alerts

Where enabled by route type or trip configuration, the assigned route/service area should act as a route geofence for live execution.

Rules:

- The system continuously compares vehicle location against the authorised route/path/service area.
- If the vehicle deviates beyond the configured threshold, TripHub should generate a real-time Route Deviation alert.
- The trip info card should flag the vehicle/trip as off-route or unauthorised route.
- Deviation events must be logged for reporting and compliance.
- The threshold, grace period and alert severity should be configurable or defined by the existing alert engine.
