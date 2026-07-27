## 31. Analytics and Audit Events

Recommended analytics events:

| Event | Key properties |
|---|---|
| `home_viewed` | role, organisation type, onboarding state |
| `home_status_selected` | status, count, destination |
| `home_onboarding_action` | task, action, previous status |
| `home_onboarding_skipped` | task, permission context |
| `home_invite_opened` | source |
| `home_invites_submitted` | row count, success count, failure count |
| `home_role_create_selected` | source |
| `home_issue_filter_selected` | issue, result count |
| `home_problem_search` | result count; do not log raw sensitive identifiers |
| `home_problem_exported` | filter set, row count, asynchronous flag |
| `home_insight_selected` | insight type, affected count |
| `home_quick_access_selected` | item, destination |
| `home_license_manage_selected` | license summary state |
| `home_widget_failed` | widget, safe error category |

Audit records are required for:

- Invitations sent or resent.
- Role assignments.
- Onboarding skip actions if operational governance requires them.
- Sensitive exports.
- Impersonated administrative activity.

---
