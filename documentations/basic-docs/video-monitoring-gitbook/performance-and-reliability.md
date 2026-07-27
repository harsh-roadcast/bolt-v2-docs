## 23. Performance and Reliability

### 23.1 Stream Load Management

- Streams should be paginated and loaded in chunks.
- A page view can contain up to 50 stream cards.
- All eligible streams on the current page view, up to 50, can be played simultaneously.
- Bulk start should be orchestrated to avoid network spikes, but the end state should allow all eligible streams on the page to play together.
- Streams outside the current paginated page should not continue consuming live-stream resources unless explicitly supported later.
- Streams outside the visible viewport may be optimised or deprioritised only if it does not break the requirement that all streams on the current page can be played simultaneously.
- Failed streams should not retry indefinitely.

### 23.2 Command Center Performance Targets

| Metric | Target |
|---|---|
| Initial page shell load | Under 3 seconds on standard broadband. |
| Stream card state update | Under 2 seconds after backend state change. |
| Filter application | Under 1 second for current loaded dataset. |
| Incident insight update | Near real time, target under 10 seconds after event ingestion. |
| Stream recovery feedback | Visible within 5 seconds of stream failure detection. |

### 23.3 Incident Page Performance

- Incident cards should lazy-load thumbnails.
- Incident video should load only when opened or played.
- Heat-map should aggregate server-side for large datasets.
- View All Incidents should use pagination or virtual scrolling.

---
