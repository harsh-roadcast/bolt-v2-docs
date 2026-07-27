## 36. Integration Dependencies

| Dependency | Map usage | Required behavior |
|---|---|---|
| Telemetry/location service | Live position, speed, heading, ignition and freshness | Return timestamped data and a resolved freshness state; support incremental updates. |
| Device-group and vehicle service | Entity identity, hierarchy, capability and linked metadata | Enforce organisation scope and return capability flags used to gate actions. |
| Geocoding service | Address search and reverse-geocoded last location | Fail independently from raw coordinates and expose unavailable/loading states. |
| Map provider | Tiles, zoom, pan, search and overlays | Support provider-failure fallback messaging and preserve non-map list/table access. |
| Geofence/POI service | Geometry, visibility, state and linked entities | Validate geometry server-side and return auditable create/update results. |
| Path/history service | Historical positions, stops, idle, events and playback | Return ordered points with timestamps and explicit no-data/error outcomes. |
| Command service | Parking Mode, immobilise and mobilise | Provide idempotency, status progression, acknowledgement and failure reasons. |
| Share-token service | Temporary tracking links and token logs | Enforce entity scope, link type, expiry and revocation server-side. |
| Driver service | Driver search, assignment and logs | Prevent invalid concurrent assignment and return auditable change history. |
| Video Monitoring | Map-level stream access | Expose only licensed channels for users with video permission. |
| EV/BMS service | Battery, charging and BMS entry | Return value freshness and unsupported/unavailable states. |
| Audit and analytics services | Sensitive action traceability and usage events | Receive actor, target, action, result and timestamps without leaking restricted data. |

Every integration failure must map to a defined user-facing state. A successful HTTP response alone must not be treated as a successful command unless the domain service confirms the intended final state.

---
