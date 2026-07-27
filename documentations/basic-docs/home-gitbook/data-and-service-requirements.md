## 24. Data and Service Requirements

### 24.1 Required services

| Service | Home dependency |
|---|---|
| Identity and organisation | User, role, organisation, hierarchy, and impersonation context. |
| Onboarding | Task state, progress, skipped state, and completion policy. |
| Device Groups | Moving, Idle, Stopped, Breakdown, and Inactive counts. |
| Device health | Score, categories, primary issues, and affected-device totals. |
| Telemetry | Last packet, GPS, RSSI, satellites, power, and reporting freshness. |
| Insights | Prioritized insight text, evidence, and destination filter. |
| Problem vehicles | Search, filters, sorting, pagination, and export. |
| Users and invitations | Invite validation, role assignment, and invitation state. |
| Roles | Assignable roles and Create New Role permission. |
| Reports | Successful-report event for onboarding completion. |
| Billing and licenses | Active, expiring, unassigned, and auto-renew-off counts. |
| Support configuration | Phone, email, address, and Contact Us destination. |

### 24.2 Aggregation

- Summary APIs should return pre-aggregated counts.
- Health responses should include a shared calculation timestamp.
- The Problem Vehicles endpoint should support server-side query parameters.
- Home should not download every device to calculate cards.
- Organisation scope must be included in or derived securely for every request.

### 24.3 Recommended response metadata

Each operational response should include:

- Organisation identifier.
- Generated-at timestamp.
- Data-as-of timestamp.
- Calculation or rules version where relevant.
- Partial-data indicator.
- Permission-safe navigation context.

---
