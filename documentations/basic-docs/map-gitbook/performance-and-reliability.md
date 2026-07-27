## 33. Performance and Reliability

Map must remain usable for large fleets.

Requirements:

- Use marker clustering for high entity counts.
- Avoid rendering full tables without pagination/virtualization.
- Debounce search/filter input.
- Avoid unnecessary full-map re-renders.
- Use backend filtering for large organisations.
- Keep selected entity context stable during refresh.
- Degrade gracefully when map tiles, geocoder or telemetry APIs are slow.
- Use lazy loading for details tabs such as sensors/video where possible.
- Load map tiles, list data and live telemetry independently so one slow dependency does not block the entire workspace.
- Preserve the last valid marker position and freshness state during short telemetry interruptions.
- Retry transient read failures with bounded backoff; do not automatically retry safety-critical write commands unless the command service confirms that retry is idempotent.
- Cancel or ignore stale requests when the user changes organisation, tab, search or filter state before an earlier request completes.
- Avoid duplicating markers, paths or command feedback when sockets reconnect or requests are replayed.
- Instrument map load, marker render, filter response, right-panel load, path replay generation and command completion times.
- Define measurable production targets for initial map readiness, live-update latency, filter response, path replay generation and command acknowledgement before release.

---
