## 20. Data Model

### 20.1 Main Entities

| Entity | Purpose |
|---|---|
| Device Group | Vehicle/asset/person grouping visible to the user. |
| Video Device | Dashcam or video hardware associated with a device group. |
| Camera Channel | Individual video stream channel on a device. |
| Stream Session | Active or attempted live-stream connection. |
| Incident | AI/system-generated safety or device event. |
| Evidence Clip | Video segment associated with an incident or recording. |
| Snapshot | Still image captured from a stream. |
| Device History Request | Historical video fetch request for channel/time range. |
| AI Insight | Real-time insight shown in Command Center. |
| Hotspot | Aggregated location with repeated incidents. |
| User Action Audit | Record of sensitive video actions. |

### 20.2 Stream Session Fields

Minimum fields:

- Stream session ID.
- Device ID.
- Device group ID.
- Channel ID.
- User ID.
- Organisation ID.
- Status.
- Started at.
- Stopped at.
- Last heartbeat.
- Error code/message.
- Data rate.

### 20.3 Incident Fields

Minimum fields:

- Incident ID.
- Event type.
- Incident name.
- Severity.
- Device ID.
- Device group ID.
- Channel ID.
- Vehicle number.
- Driver ID/name where available.
- Timestamp.
- Location coordinates.
- Address.
- Evidence clip ID.
- Thumbnail URL.
- Status.
- Created at.
- Last updated.

---
