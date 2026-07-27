## 27. Navigation and Deep-Link Rules

Every Home action must define:

- Destination module.
- Required permission.
- Organisation context.
- Filter or entity context.
- Return behavior.

### 27.1 Context preservation

- Status-card navigation should preserve the selected status.
- Insight navigation should preserve the issue category.
- Problem-vehicle View should preserve the selected entity.
- Manage should open the relevant license view.
- Report onboarding should open the correct report entry point.

### 27.2 Return to Home

When the user returns:

- Refresh onboarding state after a completion event.
- Preserve non-stale table preferences where appropriate.
- Do not restore an already completed invitation dialog.
- Update counts rather than relying on cached visual state.

---
