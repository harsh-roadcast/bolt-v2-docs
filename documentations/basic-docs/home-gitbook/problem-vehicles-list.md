## 19. Problem Vehicles List

Problem Vehicles identifies the distinct devices or vehicles with one or more active issues.

### 19.1 Summary

The table header includes:

- Number of distinct affected devices.
- `Sorted by health score`.
- Issue filter pills.
- Search.
- Filters.
- Columns.
- Export.

### 19.2 Default sorting

- Health score is sorted ascending by default.
- The lowest health value appears first.
- A visible label communicates the active sort.
- User-selected sorting may remain until refresh or explicit reset.
- Server-side sorting is required for large datasets.

### 19.3 Approved issue filters

- All problems.
- Not Reporting.
- Power Issue.
- Delayed Packet.
- Poor GPS.
- Invalid GPS.
- Poor Network.

Each filter may show the current issue count.

### 19.4 Filter behavior

- Selecting a filter updates table rows and the result count.
- Filter counts remain scoped to the organisation.
- A device can match more than one issue filter even though the distribution chart counts only its primary issue.
- Returning to All problems clears the issue filter.
- Search, advanced filters, sorting, and pagination must work together.
- Active filter state should be visible and resettable.

### 19.5 Search

Search should match supported identifiers such as:

- Vehicle name or registration.
- Device name.
- IMEI or device identifier.

Search must:

- Debounce requests.
- Ignore leading and trailing spaces.
- Preserve active issue filters.
- Show a no-result message that includes the query.
- Avoid exposing identifiers the user cannot view.

### 19.6 Approved table data

| Column | Purpose |
|---|---|
| Vehicle | Vehicle, device name, registration, model, or identifier. |
| Status | Current operating or connectivity status. |
| Last Update | Relative and absolute freshness context. |
| GPS | GPS quality, validity, and last known coordinates where permitted. |
| RSSI / SAT | Network strength and satellite count. |
| Health | Numeric device health with visual severity. |
| Issue | Primary issue and an indication of additional active issues. |

### 19.7 Row behavior

- A row may expose a `View` action.
- View should open the approved device or vehicle detail destination.
- The destination must preserve the source issue context where possible.
- Coordinates and identifiers must follow privacy and permission rules.
- A row with multiple issues may show `+n more`.

### 19.8 Columns control

- Users can show or hide optional columns.
- Required identity and action columns cannot be removed.
- Column preferences may be saved per user.
- Hidden columns must not be removed from an export unless export policy explicitly follows visible columns.

### 19.9 Export

- Export uses the active organisation, filters, search, and sorting.
- Product must define whether export includes all matching rows or the current page.
- Large exports should run asynchronously.
- The export must include generation time and applied filter metadata where feasible.
- Export permission must be enforced by the API.

### 19.10 Pagination

- Pagination is server-side for large organisations.
- Changing page preserves filter and sort state.
- Changing a filter resets to the first page.
- The result summary states the visible and total record counts.

---
