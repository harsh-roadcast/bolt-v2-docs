## 12. My Device Groups

My Device Groups provides a top-level count of operational status across the permitted fleet.

### 12.1 Approved status cards

| Status | Meaning |
|---|---|
| Moving | The linked entity is reporting movement according to the configured movement rule. |
| Idle | The entity is stationary while the engine or ignition condition indicates idle. |
| Stopped | The entity is stationary and does not meet the idle rule. |
| Breakdown | The entity has an active breakdown state from the approved operational source. |
| Inactive | The entity is inactive, unassigned, or outside the valid reporting rule. |

### 12.2 Count rules

- Each entity must be counted in only one primary status.
- Counts must respect organisation hierarchy and user permissions.
- The backend should provide aggregated counts.
- The browser must not calculate totals by loading the full device list.
- The status timestamp or freshness used to classify an entity must follow one shared backend rule.
- Unknown data must not be silently classified as Moving, Idle, or Stopped.

### 12.3 Interactions

- `View All` opens the relevant Groups or Device Groups list.
- A status card may open the destination list with the selected status applied.
- Navigation should preserve the active organisation.
- Restricted destinations must be hidden or disabled.

### 12.4 Widget states

| State | Expected behavior |
|---|---|
| Loading | Show five stable skeleton cards. |
| No groups | Show zero counts and a clear Add Device or Create Device Group path where permitted. |
| Partial failure | Show an inline error inside this widget only. |
| Stale summary | Show last-updated context when freshness exceeds the accepted threshold. |

---
