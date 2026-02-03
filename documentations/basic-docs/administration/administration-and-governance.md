# Administration & Governance

#### RBAC & Permission Guardrails

The platform enforces strict **Role-Based Access Control (RBAC)**.

* **URL Protection:** If a Client User manually types an Admin-only URL (like `/admin/device-models`), the system returns a **403 Forbidden** error and logs the attempt.
* **Inheritance:** Custom roles can be created at the Parent level and pushed down to all Child Branches.

#### Impersonation & Audit Trails

To assist with support and debugging, Admins have the ability to "Impersonate" users.

* **Security Protocol:** An Admin cannot change a client's password directly; they must first use the **Impersonate** feature.
* **Audit Trail:** Every action performed during an impersonation session is logged with a specific flag: `User [Admin_ID] performed [Action] on behalf of [Client_ID] at [Timestamp]`.

#### Permission Matrix

<table data-header-hidden data-full-width="false"><thead><tr><th width="140"></th><th></th><th></th><th></th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Role</strong></td><td><strong>Live Tracking</strong></td><td><strong>Manage Users</strong></td><td><strong>Manage Billing</strong></td><td><strong>Create Geofence</strong></td><td><strong>View Reports</strong></td><td><strong>Purchase License</strong></td><td><strong>Admin Actions</strong></td></tr><tr><td><strong>Admin</strong></td><td>✔️</td><td>✔️</td><td>✔️</td><td>✔️</td><td>✔️</td><td>✔️</td><td>✔️</td></tr><tr><td><strong>Dispatcher</strong></td><td>✔️</td><td>❌</td><td>❌</td><td>✔️</td><td>✔️</td><td>❌</td><td>❌</td></tr><tr><td><strong>Guard</strong></td><td>✔️</td><td>❌</td><td>❌</td><td>❌</td><td>❌</td><td>❌</td><td>❌</td></tr><tr><td><strong>Manager</strong></td><td>✔️</td><td>✔️</td><td>✔️</td><td>✔️</td><td>✔️</td><td>✔️</td><td>✔️</td></tr><tr><td><strong>Warehouse Staff</strong></td><td>✔️</td><td>❌</td><td>❌</td><td>✔️</td><td>❌</td><td>❌</td><td>❌</td></tr><tr><td><strong>Financial Manager</strong></td><td>❌</td><td>❌</td><td>✔️</td><td>❌</td><td>✔️</td><td>✔️</td><td>✔️</td></tr></tbody></table>

<p align="center"><sup>Table 1: Graph regarding the allowed actions as per role</sup></p>

* **Roles** are listed in the first column.
* Each **permission** (e.g., "Live Tracking," "Manage Users," etc.) is represented as a column.
* **✔️** indicates that the role has permission for that action, while **❌** indicates no permission.
* **Admin Actions** are actions that admins can take, like modifying permissions, managing system-wide settings, etc.

#### Suspension Logic

**The "On-Trip" Case:** If an Admin suspends a driver while they are currently **ON\_TRIP**, the Driver App will log them out immediately. The session is terminated for security, and the trip state handling (auto-closing or pausing) is handed over to the **TripHub** backend logic.

