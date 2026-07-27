## 10. Device Groups List

### 10.1 List Content

Each Device Group card should show:

- Status indicator.
- Device group name.
- Linked vehicle number or owner name, where available.
- Last updated time.
- Last known address.
- Pin/unpin or focus action where supported.
- Share shortcut where supported.
- Selected state when the card is active.

### 10.2 Status Filters

Status chips should show counts and filter the list and map. Filters should include all configured statuses available to the user, such as all, moving, idle, stopped, inactive and breakdown.

Rules:

- Selecting a status chip filters both the list and visible map markers.
- Count chips should be based on the currently selected hierarchy and applied high-level filters.
- Search should work within the selected tab and should not remove the active tab context.
- Refresh should reload list and map data without resetting the active tab unless a hard refresh is required.

### 10.3 Default Sorting

Device Groups should be sorted by **Last Updated**, most recent first, unless the user applies another sort. Stale/no-data entities should move lower unless filtered explicitly.

### 10.4 Marker and List Status Parity

The status shown in the left list, map marker, table row and right-side info card must use the same status source and freshness rules.

Rules:

- A marker and its corresponding list card must never show conflicting statuses for the same timestamp.
- If the list says Inactive, the marker should use the inactive marker state even if the last known speed was moving.
- If a user applies a status filter, both list cards and map markers should reduce to the same filtered entity set.
- Marker tooltips should show the entity name, status, speed where applicable, last updated time and last known address.
- For large fleets, status counts should be computed against the active organisation/hierarchy scope, not only the current visible viewport.

---
