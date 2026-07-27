## 6. Users and Permissions

### 6.1 Primary users

- **Organisation Admin:** completes setup, invites users, monitors device health, and manages licenses.
- **Fleet Operator:** reviews operating status, health issues, insights, and problem vehicles.
- **Support or Implementation User:** validates setup and investigates data-quality issues while assisting an organisation.
- **Organisation Owner:** reviews high-level status, subscription risk, and next actions.
- **Roadcast Admin:** views an organisation in the correct impersonation context where this capability exists.

### 6.2 Permission principles

- Every metric must be calculated within the user's permitted organisation scope.
- Actions must be validated at both UI and API level.
- A user must not see restricted operational or billing data through Home.
- A deep link must not send the user to a destination they cannot access.
- Hidden actions are preferred when the capability is irrelevant to the user.
- Disabled actions with an explanation are preferred when visibility helps the user understand that administrator access is required.

### 6.3 Suggested permissions

| Capability | Suggested permission |
|---|---|
| Open Home | `home:view` |
| View device-group status | `device_group:view` |
| View device health | `device_health:view` |
| View problem vehicles | `device_health:view_problems` |
| Export problem vehicles | `device_health:export` |
| Add devices | `device:manage` |
| Invite users | `user:invite` |
| View or create roles | `role:view` / `role:manage` |
| Generate a report | `report:generate` |
| Create an organisation | `organisation:create` |
| Create device groups | `device_group:manage` |
| View licenses | `license:view` |
| Manage plans and billing | `billing:manage` |

---
