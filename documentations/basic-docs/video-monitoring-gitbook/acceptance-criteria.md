## 26. Acceptance Criteria

### 26.1 Command Center

- Users can open Command Center and see accessible stream cards.
- Streams are loaded through pagination/chunking rather than loading all accessible streams at once.
- A page view can show up to 50 stream cards.
- Users can play all eligible streams on the current page view simultaneously, up to 50 streams.
- Users can switch supported grid layouts.
- Users can start and stop all eligible streams on the current paginated page view.
- Stream cards show clear live, connecting, offline, failed and reconnecting states.
- Users can retry failed streams.
- Users can search, sort and filter streams.
- Default stream sorting is based on `Last Updated`, with the most recently updated stream shown first.
- Streams with an active real-time incident are highlighted with a red border around the stream box.
- Empty filter state clearly explains that no videos match current filters.
- AI Insights panel shows live event feed, fleet distribution and stream/device status summaries.
- AI Insights are populated using active incidents, stream health, device status, hotspot and repeated-event signals.
- Clicking relevant insights focuses or filters the related stream/incident context.
- Fullscreen mode preserves the current stream layout.

### 26.2 Stream Actions

- Users can capture snapshots where channel and permissions allow it.
- Snapshot success state is displayed.
- Users can start/stop recording where supported.
- Users can initiate and disconnect intercom calls where supported.
- Unsupported actions are hidden or disabled.
- Sensitive actions are auditable.

### 26.3 Device History

- Users can open Device History from an eligible stream/device.
- Required inputs are visible and validated.
- Historical video can be generated for a valid channel/time range.
- Users can review historical stream playback and incident/event markers for the selected time range.
- Users can jump from an incident/event marker to the relevant timestamp in the historical stream.
- Empty, no-data and failure states are handled clearly.
- Users can download generated history where permitted.
- BIRA/event highlights do not block the base history flow.

### 26.4 PAP Incidents

- Users can open PAP Incidents and view recent incidents.
- Incident cards show thumbnail, severity, name, time, device/group and location.
- Users can open incident details.
- Users can view all incidents and apply filters.
- Applied filters are visible and removable.
- Incident details show evidence video, metadata and location.
- Evidence download works only for permitted users.
- Heat-map and hotspots reflect incident data and active filters.
- Empty state appears correctly when no incidents exist.

### 26.5 Permissions and Security

- Users see only authorised device groups, channels and incidents.
- Restricted evidence cannot be accessed through direct URLs.
- Downloads and intercom actions are logged.
- Stream sessions are stopped when permissions are revoked or user session ends.

---
