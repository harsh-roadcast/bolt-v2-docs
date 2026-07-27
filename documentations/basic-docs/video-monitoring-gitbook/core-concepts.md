## 8. Core Concepts

### 8.1 Device Group

A monitored entity such as a vehicle, crane, asset or other configured group. A device group may have one or more camera channels.

### 8.2 Camera Channel

An individual stream source from a dashcam or video device. A device may support multiple channels such as road-facing, driver-facing, side or rear camera.

### 8.3 Stream Session

A live connection between Bolt and a selected camera channel. Stream state is temporary and may change independently from the vehicle's GPS or ignition status.

### 8.4 Incident

A system-generated safety or device event produced by the dashcam/AI pipeline. Examples include lane departure, driver distraction, forward collision warning, driver not in view, seat belt event and vehicle too close.

### 8.5 Evidence Clip

A video segment associated with an incident. Evidence clips must preserve the timestamp, device, channel, location and event metadata.

### 8.6 AI Insight

A real-time analytical signal shown inside Command Center. It may represent a live event, stream-specific risk, fleet distribution trend or incident hotspot.

AI Insights are derived from live dashcam events, stream health, vehicle/device status and incident metadata. They should help the operator understand where attention is required without changing the default stream-grid order.

### 8.7 Active Real-Time Incident

An active real-time incident is an incident currently being detected or reported by a live dashcam stream. While active, it must be visible on the corresponding stream card and highlighted with a red border around the stream box.

---
