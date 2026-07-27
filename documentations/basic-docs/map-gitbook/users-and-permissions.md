## 6. Users and Permissions

### 6.1 Primary Users

- **Fleet Operator:** monitors live locations, filters map, reviews status and opens path replay.
- **Fleet Admin:** manages geofences, POIs, KML, drivers, sharing and commands.
- **Support/Admin User:** impersonates or supports organisations, reviews data, validates device state and troubleshoots issues.
- **Organisation Owner:** views fleet status and uses high-level tracking features.

### 6.2 Permission Requirements

Permission checks must be enforced at API and UI level.

| Capability | Suggested permission |
|---|---|
| View Map | `map:view` |
| View device groups / vehicles | `device_group:view` |
| View geofences | `geofence:view` |
| Create/edit/delete geofences | `geofence:manage` |
| View POIs | `poi:view` |
| Create/edit/delete POIs | `poi:manage` |
| View path replay | `path_replay:view` |
| Share tracking links | `tracking_share:manage` |
| View share tokens/logs | `tracking_share:view_tokens` |
| Assign driver | `driver_assignment:manage` |
| Parking mode | `parking_mode:manage` |
| Immobilize/mobilize | `remote_command:immobilize` / `remote_command:mobilize` |
| Bulk actions | Relevant entity-level bulk permission |
| Download table data | `map:download` |
| KML upload/manage | `kml:manage` |
| View video stream in map card | `video_monitoring:view` |
| View EV/BMS details | `bms:view` |

Restricted users should either not see unauthorized actions or should see them disabled with an explanatory tooltip. Critical commands such as immobilize and mobilize must never rely on UI-only permission checks.

---
