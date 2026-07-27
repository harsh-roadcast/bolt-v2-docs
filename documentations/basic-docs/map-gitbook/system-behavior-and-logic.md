## 30. System Behavior and Logic

### 30.1 Data Refresh

- Map should refresh live positions on the configured polling/socket interval.
- List cards should update when new location/status packets arrive.
- Right panel should update selected entity details without closing.
- If selected entity becomes unavailable, show stale/unavailable state rather than clearing the panel abruptly.

### 30.2 Sorting

Default sort for Device Groups should be **Last Updated, most recent first**. Additional sort options may include status, name, speed, distance and health/risk where supported.

### 30.3 Filtering and Pagination

- Backend filtering is preferred for large fleets.
- Frontend-only filtering may be used only where data volume is already bounded.
- Pagination should preserve selected tab, search, filters and sort.
- Map markers should represent the active filter scope. If the implementation only plots current page entities, the UI must make that explicit.

### 30.4 Clustering

- Markers should cluster at lower zoom levels.
- Cluster count should represent visible entities in the current filter scope.
- Clicking a cluster should zoom into the cluster area.
- Cluster color may reflect severity/status mix if implemented.

### 30.5 Selected Entity State

- Clicking a card or marker selects the entity.
- Selected entity should be visually highlighted in list and map.
- Right panel should open with selected entity details.
- Previous/Next controls should move through the current filtered list.

### 30.6 Legend and Data Freshness Logic

- Status should be calculated using the most recent valid telemetry packet and configured status thresholds.
- If telemetry timestamp exceeds the inactive/stale threshold, status should resolve to Inactive or stale/no-data even if the last known motion state was Moving.
- Marker legend, list chip, table badge and info-card status should use the same resolved status.
- If heading is missing, invalid or stale, the marker must not rotate based on old heading.
- When a selected entity receives a fresher packet, update marker position, list row/card, tooltip and right-panel values together to avoid mismatched information.

### 30.7 Remote Command Feedback Logic

- Remote commands should move through clear states: initiated, queued, sent, acknowledged, completed, failed and expired where backend supports these stages.
- The UI should not mark a command successful until backend/device acknowledgement confirms the final state.
- Command Log should record requested action, target entity, requested by, requested at, status, response reason and final timestamp.
- If a command is queued because the device is offline or unsafe to execute immediately, the UI must clearly say that the command is queued and not yet completed.
- Critical commands such as immobilize/mobilize should require confirmation and should respect speed/safety rules defined for that command.

---
