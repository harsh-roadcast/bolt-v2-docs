# Getting Started

#### Authentication and Security

Access is gated by a multi-layered security protocol:

* **Credentials:** Unique username and password mapped to your organization.
* **MFA/OTP Verification:** A secondary security layer requiring a one-time password sent via registered email or SMS.
* **Instant Session Invalidation:** The system utilizes a "Session Versioning" strategy. If an account is suspended, all active JSON Web Tokens (JWT) are blacklisted instantly, terminating sessions across all browsers and mobile apps.

#### Workspace Selection & Context Switching

Because a single user can be a member of multiple organizations, the **Select Organisation** screen appears immediately after login.

* **Contextual Filtering:** Once a workspace is selected, the entire application (Maps, Reports, Billing) is filtered to show only data belonging to that specific node.
* **Role Fluidity:** You may hold an "Admin" role in a regional Child Branch while having only "Viewer" permissions in the main Parent Organization.

