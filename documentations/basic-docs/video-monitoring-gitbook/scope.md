## 5. Scope

### 5.1 In Scope

- Command Center page.
- PAP Incidents page.
- Live stream grid layouts.
- Stream All and Stop All Streams actions.
- Per-channel stream actions.
- Stream health states and retry behavior.
- Search, sort and filters for streams.
- Favourite stream filtering.
- AI Insights panel with live event feed and fleet distribution.
- Device group status and stream status summaries.
- Intercom/call-to-device workflow.
- Snapshot capture.
- Recording start/stop and save confirmation.
- Device History generation and playback.
- View on Map workflow.
- PAP incident cards, severity metrics, filters and search.
- Incident detail page with video playback, metadata and location.
- Incident heat-map and hotspot list.
- Event reference guide.
- Download actions where available.
- Basic evidence and audit traceability.

### 5.2 Out of Scope for Initial Release

- Full video editing.
- Manual incident creation without device evidence.
- Public share links for incident videos.
- AI chat/copilot over all videos.
- Automated coaching workflows.
- Advanced privacy masking configuration UI.
- Billing configuration for video storage.
- Mobile Video Monitoring authoring flows.
- False incident handling, incident verification and incident correction workflows. These will be defined in a separate sprint.
- Escalation actions that depend on false-positive review or manual incident validation.

### 5.3 Confirmed Product Decisions

- Streams are paginated and loaded in chunks instead of loading the full stream universe at once.
- A single page view can contain up to 50 stream cards.
- All eligible streams in the current page view, up to 50, can be played simultaneously.
- Default stream sorting is based on `Last Updated`, with the most recently updated devices/streams first.
- Streams with active real-time incidents are highlighted using a red border around the stream box.
- False-incident handling is intentionally excluded from this release and will be handled in another sprint.

---
