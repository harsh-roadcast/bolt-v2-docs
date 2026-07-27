## 40. Resolved Product Decisions

- The documented product interface is the source of truth for current layout, labels and visible interaction states.
- Map is the core Bolt operational workspace and should not be treated as a simple visual tracking page.
- The primary page structure is left panel + map canvas + right details panel.
- Groups, Geofence and POI are the primary Map tabs.
- Device Groups default sorting should be Last Updated, most recent first.
- Path Replay and Show Trail are separate flows: Path Replay is full historical playback, Show Trail is quick map-level recent movement visibility.
- Immobilize must be speed-sensitive and can enter queued state when vehicle speed is above threshold.
- Shared tracking links must be tokenized and expiry-aware.
- Geofence visibility and geofence enablement are separate concepts.
- Explicit product and safety rules in this PRD supersede a purely visual interpretation of the interface.

---
