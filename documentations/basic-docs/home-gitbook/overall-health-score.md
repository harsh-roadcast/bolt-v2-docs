## 16. Overall Health Score

Overall Health Score summarizes the organisation's permitted device health on a `0–100` scale.

### 16.1 Display

The approved card contains:

- Overall Health Score heading.
- Information control.
- Semicircular gauge.
- Numeric score.
- `OUT OF 100` label.
- Health classification badge.
- Total, Healthy, Needs Attention, and Unknown counts.
- Supporting explanation.

### 16.2 Health categories

| Category | Expected interpretation |
|---|---|
| Healthy | Device meets the approved reporting, GPS, power, and network health rules. |
| Needs Attention | One or more active signals reduce confidence or operational reliability. |
| Unknown | Health cannot be determined because required data is missing or unsupported. |

`Total` must equal `Healthy + Needs Attention + Unknown` for the same scope and calculation timestamp.

### 16.3 Score contract

- The score is calculated by a backend service.
- Home receives the score, classification, contributing totals, calculation version, and freshness timestamp.
- The client must not recreate the score from table rows.
- The score must be clamped to the valid range.
- The gauge, number, badge, and totals must come from one response version.
- A calculation change should be versioned so support and QA can explain differences.

### 16.4 Classification

The approved design includes `STRONG`. Additional classifications and thresholds must be supplied by the score service and confirmed before release.

Home must not hard-code a threshold that can drift from backend logic.

### 16.5 Information control

The information control should explain:

- What the score represents.
- Which broad signal groups contribute.
- When the score was last calculated.
- That the score applies only to the current organisation scope.

---
