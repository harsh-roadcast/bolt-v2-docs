## 33. QA Scenario Matrix

| Scenario | Expected result |
|---|---|
| New organisation with no devices | First-time state, onboarding visible, no false health score. |
| Devices exist and no task is complete | Device-data state with `0 of 3 complete`. |
| Two onboarding tasks complete | Invite entry shows `2 of 3 complete`. |
| Invite opened | Modal appears and background is non-interactive. |
| Role list opened | Assignable roles and Create New Role appear according to permission. |
| Invalid email entered | Row-level error; Send Invites remains unavailable. |
| One of three invitations fails | Successful rows resolve; failed row remains with explanation. |
| All onboarding tasks complete | Checklist is removed and health widgets move upward. |
| No device issues | Healthy empty states; no problem rows. |
| Issue filter selected | Matching devices appear and count updates. |
| Organisation changes during load | Previous responses are ignored. |
| License permission missing | License data and Manage follow the approved restricted policy. |
| Insights service fails | Other health data remains available with an insight-level fallback. |
| Large fleet | Summary APIs and server-side table operations prevent browser overload. |

---
