## 12. Stream Actions

### 12.1 Snapshot

Users can capture a snapshot from a camera channel.

![Take Snapshot flow](../../.gitbook/assets/take_snapshot.png)

*Live stream workspace with the channel-level snapshot action and its related state.*

Rules:

- Snapshot action is available only when the channel is live or has a valid current frame.
- The system should show success feedback such as `Snapshot saved in Events`.
- Snapshot must store device group, channel, timestamp, user and organisation.
- Snapshot should be accessible later from the relevant evidence/event area where supported.

### 12.2 Recording

Users can start and stop recording where the device and permissions allow it.

![Recording flow](../../.gitbook/assets/recording.png)

*Device History recording controls, active-recording state and saved-recording feedback.*

Rules:

- Start recording should show immediate feedback.
- Stop recording should show saved confirmation.
- Recording duration should respect system limits.
- Saved recording must preserve metadata and audit user action.
- If recording fails, show clear failure reason.

### 12.3 Call / Intercom

Users can initiate a voice connection with a supported device.

![Call device and intercom flow](../../.gitbook/assets/call_device.png)

*Call-device workflow showing the stream context and intercom control states.*

Supported interface states include:

- Connect.
- Connecting.
- Speak Now.
- Mic on/off.
- Speaker on/off.
- Disconnect.
- Connection error.

Rules:

- Call action is available only for devices that support intercom.
- Only authorised users can initiate calls.
- The UI should prevent more than one active call to the same device from the same user session.
- Connection failure must be recoverable without refreshing the page.
- Disconnect should terminate the session cleanly.

### 12.4 View on Map

Users can move from a live stream to map context.

![View stream on map](../../.gitbook/assets/view_on_map.png)

*Map context for a selected video-enabled vehicle, with its streaming panel preserved.*

Rules:

- The map should focus the selected device group/vehicle.
- Vehicle status and location should remain visible.
- The Video Streaming tab should show available channels.
- Returning to Command Center should preserve prior stream layout where technically feasible.

---
