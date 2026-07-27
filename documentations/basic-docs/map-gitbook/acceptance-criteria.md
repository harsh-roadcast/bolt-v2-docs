## 38. Acceptance Criteria

### 38.1 Base Map

- User can open Map and see accessible device groups on the map.
- User can switch between Groups, Geofence and POI tabs.
- User can search and filter within each tab.
- Selecting a list item focuses the map and opens the right panel.
- Selecting a marker opens the correct entity details.
- Default Device Group sorting is Last Updated, most recent first.

### 38.2 Details and Actions

- Right panel shows correct overview and sensor data for selected entity.
- Unsupported sensor fields show N/A or equivalent unavailable state.
- Action menu shows only permitted and supported actions.
- Share link generation supports expiry and token log.
- Driver assignment supports assigned, unassigned and logs states.
- Parking mode supports enabled/disabled and schedule states.
- Immobilize/mobilize flows show confirmation, queued/success/failure states.

### 38.3 Path and Trail

- User can open Path Replay and select groups/path criteria.
- Path Replay shows path, stops and events where data exists.
- No-data path replay shows clear no-data state.
- Show Trail displays recent movement without requiring full Path Replay.

### 38.4 Geofence, POI and KML

- User can view geofence list and focus boundaries on map.
- User can create/edit geofence where permitted.
- User can show/hide and enable/disable geofences where permitted.
- User can view POIs and POI table.
- User can add KML and convert/link as supported by design.

### 38.5 Table and Bulk

- Vehicle, geofence and POI table views load with correct columns.
- Filters and downloads work from table view.
- Bulk selection shows selected count and permitted actions.
- Bulk share generates scoped link for selected entities.

### 38.6 Reliability, Accessibility and Audit

- List, marker, table and right-panel status remain consistent for the same telemetry timestamp.
- A stale heading never rotates a marker as if it were current.
- Map-provider or geocoder failure does not remove the equivalent entity list/table workflow.
- Keyboard users can open and close filters, details panels, action menus and confirmation dialogs without losing focus.
- Critical commands are not shown as successful before backend/device confirmation.
- Share, driver, geofence, KML, Parking Mode and immobilise/mobilise actions create the required audit entries.

---
