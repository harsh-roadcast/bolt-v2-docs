## 14. Invite Team Members Flow

The invitation flow is initiated from the onboarding checklist or the Add Users Quick Access item.

![Invite Team Members entry state](../../.gitbook/assets/home_invite_entry.png)

*The approved entry state shows two completed onboarding tasks and Invite Team Members as the remaining action.*

### 14.1 Entry behavior

- Selecting Invite opens a centered modal above the current Home state.
- The background is dimmed and must not accept pointer interaction.
- The underlying page and organisation context remain loaded.
- Keyboard focus moves into the dialog.

![Invite Users dialog](../../.gitbook/assets/home_invite_dialog.png)

*The invitation dialog captures email and role, supports additional invitees, and provides Cancel and Send Invites actions.*

### 14.2 Dialog content

The dialog includes:

- Title: `Invite Users`.
- Explanatory invitation copy.
- Required Add Email field.
- Required Role field.
- Add another team member.
- Cancel.
- Send Invites.
- Close control.

### 14.3 Email validation

- Email is required for every invite row.
- Leading and trailing spaces must be removed.
- Email format must be validated before submission.
- Duplicate email addresses within the dialog must be rejected.
- Existing organisation members must return a clear message.
- An existing pending invitation must return a clear status and approved resend behavior.
- Validation must be shown beside the relevant row.

### 14.4 Multiple invitees

- Add another team member appends a new email-and-role row.
- Each row is validated independently.
- A removable row must provide an accessible label.
- Removing a row must not change the data entered in other rows.
- Submission must clearly report full success, partial success, or complete failure.

### 14.5 Submission behavior

- Send Invites remains disabled until every active row is valid.
- Submission must prevent accidental double-click duplication.
- A loading state appears while the request is processed.
- On success, show confirmation and update the onboarding task.
- On partial success, identify which invitees failed and preserve those rows.
- Closing after success returns the user to the same Home scroll position.

### 14.6 Cancel and close

- Cancel and the close icon dismiss the dialog.
- If valid unsent information exists, the product may request confirmation before discarding it.
- Escape closes the dialog unless a submission is in progress.
- Focus returns to the control that opened the dialog.

---
