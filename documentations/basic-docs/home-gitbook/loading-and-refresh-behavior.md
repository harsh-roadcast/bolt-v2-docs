## 25. Loading and Refresh Behavior

### 25.1 Initial load

Home should load progressively:

1. Global shell and authenticated context.
2. Greeting and static layout.
3. Onboarding and Quick Access.
4. Device-group and license summaries.
5. Health, distribution, insights, and table.

### 25.2 Independent widgets

- Each data widget has its own loading state.
- A failure in licenses must not block device health.
- A failure in insights must not hide the table.
- Layout dimensions should remain stable while content loads.

### 25.3 Refresh

- Entering Home requests fresh summary data.
- Organisation changes reload all organisation-scoped widgets.
- Manual browser refresh reloads the page safely.
- If auto-refresh is introduced, it must not reset search, filter, page, column preferences, modal state, or scroll position.
- Auto-refresh must not replace an invitation form while the user is typing.

### 25.4 Stale data

- Stale data may remain visible when it is safer than showing nothing.
- Stale state must include clear freshness information.
- The client must not present stale data as live.
- A retry action should be available for failed or stale widgets where appropriate.

---
