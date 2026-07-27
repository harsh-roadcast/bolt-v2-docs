## 13. Get Started with Bolt

Get Started with Bolt is an organisation onboarding checklist that helps a new customer reach an operational baseline.

### 13.1 Approved tasks

| Task | Purpose | Primary action |
|---|---|---|
| Add Your First Device | Connect the first GPS or supported device so tracking can begin. | Create |
| Invite Team Members | Add operators or administrators and assign access. | Invite |
| Generate Your First Report | Run a report to confirm that data can be reviewed. | Generate |

### 13.2 Progress

- Progress uses the format `x of 3 complete`.
- The progress bar must match the numeric count.
- A completed task uses a clear success state.
- The next incomplete task remains actionable.
- Progress must update after a successful completion event.

### 13.3 Completion triggers

| Task | Recommended completion event |
|---|---|
| Add Your First Device | A device is successfully created or assigned to the organisation. |
| Invite Team Members | At least one invitation is successfully sent or a non-owner user is created. |
| Generate Your First Report | At least one report completes successfully. |

The exact event identifiers must be shared by the source modules and the onboarding service. Opening a destination page is not sufficient to mark a task complete.

### 13.4 Skip behavior

- Skip must require an explicit user action.
- Skip must be stored separately from completion.
- A skipped task must not claim that the underlying setup is done.
- Product policy must determine whether skipped tasks increase the visible completion count.
- If the task becomes complete later, completion should replace the skipped state.
- The user's role must permit the skip action if onboarding governance restricts it.

### 13.5 Deep-link behavior

- Create opens the device creation or device registry entry flow.
- Invite opens the Home invitation dialog.
- Generate opens Report Center at the appropriate report-generation entry point.
- Returning to Home should refresh the related onboarding task without resetting the page.

---
