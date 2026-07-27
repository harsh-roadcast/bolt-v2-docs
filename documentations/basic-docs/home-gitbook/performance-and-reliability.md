## 28. Performance and Reliability

### 28.1 Performance expectations

- Render the shell and greeting without waiting for all summaries.
- Use backend aggregation for all fleet-level counts.
- Use server-side table operations for large organisations.
- Lazy-load below-the-fold data where it improves first render.
- Avoid rendering unnecessary rows outside the visible table page.
- Cache static support configuration and permission-safe navigation metadata.

### 28.2 Reliability

- Use request cancellation when the organisation changes.
- Ignore late responses from the previous organisation.
- Use retry with controlled backoff for transient read failures.
- Invitation submission must use idempotency protection.
- Export should produce a trackable job when processing is asynchronous.

### 28.3 Data consistency

Small timing differences can occur because widgets may load independently. However:

- Totals inside one card must be internally consistent.
- Score and score categories must share a calculation version.
- Chart and issue totals should come from the same health snapshot where feasible.
- A refresh indicator should be used if the page contains mixed timestamps beyond the accepted tolerance.

---
