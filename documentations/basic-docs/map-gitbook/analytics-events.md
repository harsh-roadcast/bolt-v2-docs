## 35. Analytics Events

Analytics should measure whether users can find an entity, understand its state and complete an operational action without leaving the Map module.

| Event | Trigger | Key properties |
|---|---|---|
| `map_opened` | Map workspace becomes usable | organisation, user role, accessible entity count, initial tab, load duration |
| `map_tab_changed` | User changes Groups, Geofence or POI tab | previous tab, new tab |
| `map_entity_searched` | Search is submitted or results update | active tab, query length, result count |
| `map_filter_applied` | Basic or advanced filters are applied | filter types, active-filter count, result count |
| `map_view_changed` | User switches between map/list and table representation | previous view, new view |
| `map_entity_selected` | Card, row or marker is selected | entity type, selection source, resolved status |
| `map_details_tab_opened` | Overview, Sensors or Video tab is opened | entity type, tab, device capability |
| `map_path_replay_requested` | User submits path criteria | entity count, path type, date range |
| `map_path_replay_result` | Path replay succeeds or fails | result, position count, generation duration, failure reason |
| `map_trail_shown` | Show Trail is activated | entity count, trail window |
| `map_share_link_generated` | Tracking link is successfully created | link type, entity count, expiry duration |
| `map_driver_assignment_changed` | Driver is assigned or unassigned | action, entity type, result |
| `map_geofence_saved` | Geofence create/edit completes | action, shape type, linked-entity count, result |
| `map_kml_processed` | KML upload or conversion completes | action, file size band, geometry type, result |
| `map_parking_mode_updated` | Parking Mode settings are submitted | enabled, scheduled, result |
| `map_remote_command_requested` | Immobilise or mobilise is confirmed | command type, speed band, device state |
| `map_remote_command_result` | Remote command reaches a terminal state | command type, final status, duration, reason |
| `map_error_shown` | A user-visible error is displayed | error type, active flow, recoverable |

Analytics payloads must not include unmasked IMEI, SIM, driver phone number, public share token or precise coordinates unless explicitly approved under the organisation's analytics and privacy policy.

---
