## 36. Implementation Decisions Still Required

The approved UI does not define the following backend or policy details:

- Exact Moving, Idle, Stopped, Breakdown, and Inactive classification rules.
- Whether skipped onboarding tasks increase the visible completion count.
- Whether onboarding completion is organisation-level, user-level, or mixed.
- Health-score formula, thresholds, and all possible classification labels.
- Primary-issue priority order.
- Health data refresh interval and stale threshold.
- Whether chart selection filters the table directly.
- Whether Problem Vehicles supports one or multiple simultaneous issue filters.
- Whether table export includes all matching rows or only the current page.
- Which table-column preferences persist across sessions.
- Invitation resend and expiry policy.
- Behavior when a newly created role returns to an unsent invitation.
- Whether support details are platform-wide or organisation-specific.

These decisions should be resolved in API contracts or product configuration. They should not be inferred independently by the frontend.

---
