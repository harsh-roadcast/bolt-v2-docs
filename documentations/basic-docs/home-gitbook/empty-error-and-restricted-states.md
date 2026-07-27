## 26. Empty, Error, and Restricted States

### 26.1 No devices

- My Device Groups shows zero counts.
- Get Started prioritizes Add Your First Device.
- Health score does not show a misleading `0`.
- Distribution shows a no-device message.
- Insights explain that data will appear after devices report.
- Problem Vehicles shows a no-data state.

### 26.2 Devices but no active issues

- Health presents a healthy state.
- Distribution shows a positive empty state.
- Insights shows no critical recommendations.
- Problem Vehicles shows `No problem vehicles found`.

### 26.3 No search results

- Keep the current query and filters visible.
- Explain that no vehicles match.
- Provide a clear reset action.

### 26.4 Widget failure

- Show the error inside the affected card.
- Preserve other Home sections.
- Offer retry where useful.
- Log the service, organisation-safe context, and correlation identifier.

### 26.5 Permission restriction

- Do not fetch unauthorized data.
- Hide restricted metrics or replace them with an approved access message.
- Do not reveal restricted counts in loading placeholders, error messages, or analytics.

### 26.6 Invitation errors

- Invalid email: show row-level validation.
- Duplicate row: identify the duplicate.
- Existing user: explain that the person already has access.
- Pending invite: show current status and approved resend action.
- Role unavailable: require another valid role.
- Partial send: preserve failed rows for correction or retry.

---
