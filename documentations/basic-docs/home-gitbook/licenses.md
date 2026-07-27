## 21. Licenses

Licenses provides a compact summary of subscription and assignment health.

### 21.1 Approved metrics

| Metric | Meaning |
|---|---|
| Active | Licenses currently active under the approved billing rule. |
| Expiring Soon | Licenses within the configured expiry-warning window. |
| Unassigned | Purchased licenses not assigned to a device. |
| Auto-Renew Off | Renewable licenses or subscriptions without auto-renew enabled. |

### 21.2 Rules

- Metrics come from the billing and license service.
- Counts use the current organisation hierarchy.
- Metric definitions must match Plan & Billing.
- A license must not be counted in a misleading category because of stale billing data.
- Expiring Soon uses a backend-configured window.
- `Manage` routes to the permitted license-management destination.

### 21.3 Restricted state

If the user can view Home but cannot view billing:

- Hide the Licenses card, or
- Show only permitted status information without Manage.

The selected policy must be consistent across roles.

---
