## 6. Users and Permissions

| User | Main capability |
|---|---|
| Organisation Admin | Access all authorised device streams, incident evidence, downloads and module settings. |
| Fleet Operations User | Monitor live streams, use filters, open map context and review permitted incidents. |
| Safety Supervisor | Review PAP incidents, severity distribution, heat-map, hotspots and evidence. |
| Support/Technical User | Diagnose stream health, retry failures, verify device/channel status and use Device History. |
| Parent/Reseller Admin | Access child-organisation streams and incidents only where explicitly authorised. |

### Permission Rules

- Video access is controlled by organisation scope, device-group access and RBAC permissions.
- A user who can see a vehicle does not automatically get access to all camera channels unless video permission is granted.
- Downloading evidence requires explicit permission.
- Intercom/call actions require separate permission because they interact with the driver/device.
- Incident evidence must not be visible after a user loses access to the organisation, device group or vehicle.
- Cross-organisation monitoring is allowed only for authorised parent/reseller users.
- All sensitive actions must be auditable: snapshot, recording, download, call connection, stream retry and incident detail access.

---
