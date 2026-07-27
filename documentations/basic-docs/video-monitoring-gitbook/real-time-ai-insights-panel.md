## 11. Real-Time AI Insights Panel

The AI Insights panel provides context without requiring the user to leave Command Center.

### 11.1 Panel Content

The current interface shows:

- `Insights Engine` header.
- Live analytics cards.
- Active AI events such as forward collision, distraction, vehicle too close and seat belt event.
- Fleet distribution map.
- Device group status summary.
- Stream status summary.
- Selected stream context where applicable.

### 11.2 Live Event Cards

Each live event card should show:

- Event name.
- Severity/priority indicator.
- Live status.
- Time.
- Device or vehicle identifier.
- Optional click-through to incident details or filtered live stream.

### 11.3 AI Insight Population Logic

AI Insights should be populated from the following sources:

- Active dashcam incidents from live streams.
- Newly generated incident events from the PAP/event pipeline.
- Stream health changes such as offline, reconnecting, failed or recovered streams.
- Device group status, vehicle status and ignition/device connectivity where available.
- Location-based incident clusters and hotspots.
- Repeated incidents from the same device, driver, route, territory or organisation scope.

Priority order for insight cards:

1. Active critical incidents happening right now.
2. Active high/major incidents happening right now.
3. Multiple incidents on the same stream or device within the configured analysis window.
4. Location hotspots with repeated incidents.
5. Stream failures affecting monitoring continuity.
6. Device group or fleet distribution summaries.
7. Informational insights such as all-clear, low-risk distribution or no active event state.

Rules:

- Insights must respect the user's organisation, hierarchy and device-group permissions.
- Insights should refresh in near real time where live event data is available.
- Each insight should show a `last updated` or event timestamp so the user understands recency.
- Duplicate events from the same stream should be grouped within a configurable deduplication window.
- If the same stream has multiple active incidents, the highest-severity incident should drive the primary insight.
- Insights should not create a separate incident unless the underlying event pipeline has created or confirmed that incident.
- Clicking an insight should either focus the stream card, apply a contextual filter, open incident details or open the relevant map context.
- If no active insights are available, show an all-clear or empty insight state instead of stale incident cards.

### 11.4 Fleet Distribution

Fleet distribution should show the spatial spread of monitored vehicles/devices and use status/incident markers to indicate risk concentration.

### 11.5 Stream and Device Counts

Counts should include at minimum:

- Active.
- Idle.
- Stopped.
- Inactive.
- Live.
- Offline.
- Reconnecting.

Counts must reflect the current organisation scope and should indicate whether they are global or filtered.

### 11.6 Insight Interaction

Clicking an insight should either:

- Select the related stream in the grid.
- Filter the grid to matching incident streams.
- Open the incident detail page if evidence exists.
- Focus the related vehicle on the map.

The behavior must be predictable and should not unexpectedly stop active streams.

---
