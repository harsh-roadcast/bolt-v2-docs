## 7. Core Concepts

### 7.1 Device Group

A Device Group is the primary trackable entity in Map. It may represent a vehicle, asset, personal tracker or another linked entity. Map cards and details should show the linked vehicle/owner where available.

### 7.2 Map Entity Tabs

Map uses three primary tabs:

- **Groups:** the visible UI label for operational Device Group entities.
- **Geofence:** saved areas, boundaries and alert zones.
- **POI:** saved points of interest.

`Device Group` remains the domain/entity name in APIs, permissions, data models and this PRD. `Groups` is the shorter navigation label shown in the current product interface.

**Linked Data** and **Command Log** are related contexts and should be available where implementation supports them.

### 7.3 Entity Status and Marker Legend

Device-group status should support the core fleet states used across Bolt:

- **Moving:** valid recent packet, ignition/motion state indicates movement, and speed is above the configured movement threshold.
- **Idle:** valid recent packet, ignition is on, and the entity is not moving beyond the configured idle/movement threshold.
- **Stopped:** valid recent packet, ignition is off or the entity is stationary beyond the configured stopped threshold.
- **Inactive:** no valid recent packet within the configured inactive threshold, or device is offline/not reporting.
- **Breakdown:** vehicle is marked as breakdown through operational state, alert state or supported device/workflow logic.
- **No data / unknown:** the entity exists but the system does not have enough telemetry to determine live status.

Status counts in the list header should act as quick filters. Hover or tooltip copy should clarify the status meaning where the state is not obvious.

Marker legend requirements:

- Each status must have a distinct visual marker state that is consistently used across map markers, list chips and table status values.
- Moving markers should support direction/heading where valid heading data exists.
- Idle, stopped, inactive and breakdown markers should not imply movement unless heading/motion data is current.
- Marker labels should show the primary vehicle number/device-group name when labels are enabled.
- Cluster markers should show the number of grouped entities and should expand or zoom into the clustered area on click.
- The legend should be accessible from the map layer/control area so users can interpret marker color, marker shape and status labels without leaving the map.
- If telemetry is stale, the marker should prioritize freshness communication over last known movement state.

### 7.4 Last Updated

Last Updated represents the most recent valid packet/event timestamp received for the entity. It is central to sorting, freshness indicators and inactive-state logic.

### 7.5 Map Commands

Map commands are actions issued from the map context, such as parking mode, immobilize, mobilize, share link generation and driver assignment. Commands must have clear initiated, queued, success, failed and expired states where applicable.

---
