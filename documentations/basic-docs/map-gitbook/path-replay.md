## 17. Path Replay

### 17.1 Purpose

Path Replay allows users to review historical movement for one or more selected groups over a selected date/path window.

![Historical route, events, stops and playback controls in Path Replay](../../.gitbook/assets/path_replay.png)

*Path Replay combines route history, stop and event lists, playback speed and map-layer controls.*

### 17.2 Entry Points

Users can access Path Replay from:

- Selected vehicle/device group action menu.
- Direct Path Replay route.
- Table action where available.

### 17.3 Functional Requirements

Path Replay should support:

- Selecting one or more groups.
- Selecting path type/date option.
- Viewing name, vehicle number and status.
- Viewing path info metrics.
- Map path visualization.
- Stops tab.
- Events tab.
- Playback controls.
- Playback speed options: 1x, 2x, 3x, 4x and 5x, matching the current design.
- Opacity control.
- Follow vehicle.
- Show arrows.
- Show stops.
- Show idle.
- Show events.
- Show stream where the selected vehicle and historical interval have video data.
- Show geofence.
- Filter ignition off.
- Show start and end.
- No data state when no path is available.
- Warning toast when no position data is found.

### 17.4 No Data Behavior

If path data is unavailable:

- Show a clear no-data state.
- Disable playback controls where playback cannot run.
- Preserve selected groups and path filters so the user can adjust criteria.
- Do not show misleading zero-distance playback as successful data.

---
