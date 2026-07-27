## 13. Device History

Device History allows users to generate and review historical video for a selected device/channel/time range. It is used for both historical stream playback and incident/event review on that historical timeline.

The workflow should help users answer: what happened on this device, on this camera channel, during this time window, and whether any incidents were detected during that period.

![Device History setup](../../.gitbook/assets/device_history_setup.png)

*Device History before generation, including vehicle context, channel selection, date and time inputs.*

### 13.1 Entry Points

Device History can be opened from:

- A live stream card.
- A device group action.
- Map vehicle panel where video streaming is available.
- Incident-related workflows where historical review is needed.

### 13.2 Required Inputs

- Channel.
- Date.
- Start time.
- End time.

The UI must show validation when the user tries to generate history without selecting the required time window.

### 13.3 Device Context

The page should show:

- Device group name.
- Vehicle number.
- Number of cameras.
- Vehicle/device status.
- Ignition status.
- Last update time.
- Last known location.

### 13.4 Generate History

After the required inputs are supplied, the system should fetch the historical footage and render the player.

![Generated Device History](../../.gitbook/assets/device_history_generated.png)

*Generated history with playback, timeline availability, event markers and channel-level output.*

States:

- Empty state before time selection.
- Validation error.
- Loading/fetching state.
- Generated playback.
- No event/video found.
- Failed to fetch history.

### 13.5 Historical Stream and Incident Review

The generated history view should support:

- Historical stream playback for the selected channel and time range.
- Incident/event markers on the video timeline where incident metadata exists.
- Ability to jump from an incident marker to the relevant timestamp in the historical stream.
- Clear differentiation between generated video footage and generated incident highlights.
- Empty state when historical footage is available but no incidents are found.
- Empty state when neither footage nor incidents are available for the selected time range.
- Download of generated historical footage where user permission and device capability allow it.

Incident markers should use the incident timestamp from the event pipeline. If the incident timestamp and video timestamp differ, the system should retain both values internally and use the video timestamp for playback seeking.

### 13.6 BIRA / Event Highlights

The interface includes `Get Event Highlights with BIRA` and `Run BIRA Analysis`.

![BIRA event analysis](../../.gitbook/assets/bira_analysis.png)

*BIRA analysis entry inside Device History, with stream playback, timeline data and analysis actions.*

For the initial PRD, BIRA should be treated as an optional event-highlight analysis layer over generated history. It should not block the core Device History flow.

Rules:

- BIRA action appears only when historical video is generated.
- Analysis should show meaningful highlights if events are detected.
- If no events are found, show a clear empty state.
- Highlight timestamps should seek the player to the relevant segment.

### 13.7 Download History

Where permitted, users can download generated history output.

![Download Device History](../../.gitbook/assets/download_history.png)

*Generated Device History with per-segment playback and download actions.*

Rules:

- Downloads require permission.
- Downloaded file should include the correct device, channel and time range metadata.
- Download failure should not discard the generated history session.

---
