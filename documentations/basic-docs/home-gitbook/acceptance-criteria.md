## 32. Acceptance Criteria

### 32.1 Page and state selection

- Home opens as the configured post-login landing page.
- The correct organisation and user context are visible.
- Only Development Ready Home components are rendered.
- First-time, device-data, invitation, and completed states resolve correctly.
- Closing an overlay returns to the same underlying state.

### 32.2 My Device Groups

- Moving, Idle, Stopped, Breakdown, and Inactive are displayed.
- Counts are mutually exclusive within the approved status model.
- Counts respect organisation and permission scope.
- View All opens the correct destination.

### 32.3 Onboarding

- The first-time state shows `0 of 3 complete`.
- Progress and the progress bar remain consistent.
- Task completion comes from successful source-module events.
- Skip is stored separately from completion.
- Completed-onboarding state removes the checklist.

### 32.4 Invitations

- Invite opens the modal.
- Email and role are required.
- Multiple invite rows can be added.
- Duplicate and invalid emails are rejected clearly.
- Role options come from the current organisation.
- Create New Role is permission-controlled.
- Successful invitations update onboarding.
- Partial failure preserves unsuccessful rows.

### 32.5 Overall Health Score

- Score is displayed from `0–100`.
- Gauge, score, classification, and totals use one response version.
- Healthy, Needs Attention, and Unknown sum to Total.
- Information content explains the score at an appropriate level.
- No-device state does not present a false score.

### 32.6 Primary Issue Distribution

- Every affected device is counted once under its primary issue.
- Legend, chart, and counts match.
- Issue colors remain consistent.
- Empty state is shown when there are no active issues.

### 32.7 AI Insights

- Insight counts match the underlying device set.
- Insights are prioritized and deduplicated.
- View devices opens the correct issue context.
- A rule-based fallback is available if narrative generation fails.

### 32.8 Problem Vehicles

- The table defaults to health score ascending.
- Issue filters update rows and totals.
- Search works with active filters.
- Columns control behaves consistently.
- Pagination is preserved during compatible interactions.
- Export respects scope, filters, sorting, and permission.
- View opens the approved entity destination.

### 32.9 Utility column

- Quick Access destinations are correct.
- Restricted actions are hidden or disabled consistently.
- License counts match Plan & Billing definitions.
- Manage respects billing permission.
- Need Help uses configured contact information.

### 32.10 System behavior

- Widget failures do not block the page.
- Organisation switching cancels or ignores stale requests.
- Loading states do not cause major layout shifts.
- The page is keyboard operable.
- Charts have text equivalents.
- Invitation and export actions are auditable.

---
