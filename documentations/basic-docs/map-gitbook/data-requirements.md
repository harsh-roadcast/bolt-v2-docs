## 29. Data Requirements

### 29.1 Device Group Data

Required fields:

- Entity ID.
- Entity name.
- Entity type.
- Linked vehicle ID/number.
- Linked owner name where applicable.
- Status.
- Latitude/longitude.
- Heading.
- Speed.
- Last updated timestamp.
- Last known address.
- Organisation and hierarchy path.
- Device capability flags.
- License/module capability flags.

### 29.2 Sensor Data

Sensor values should be returned as typed fields with freshness metadata. Unsupported values should return unsupported/unavailable state rather than null-only fields.

### 29.3 Geofence Data

Required fields:

- Geofence ID.
- Name.
- Shape type.
- Geometry.
- Radius/area.
- Color.
- Enabled/disabled state.
- Visible/hidden state per user/session where applicable.
- Linked device groups.
- Created/updated metadata.
- Property schema and configured values.

### 29.4 POI Data

Required fields:

- POI ID.
- Name.
- Coordinates.
- Address.
- Icon.
- Description.
- Created/updated metadata.

### 29.5 Command Data

Required fields:

- Command ID.
- Command type.
- Target entity.
- Requested by.
- Requested at.
- Current status.
- Status reason.
- Device acknowledgement timestamp.
- Final result.
- Audit metadata.

### 29.6 Marker Legend and Navigation Data

Required fields:

- Resolved status.
- Raw motion state.
- Ignition state.
- Speed.
- Heading.
- Heading timestamp.
- Last valid packet timestamp.
- Data freshness state.
- Marker icon type.
- Marker label value.
- Cluster eligibility.
- Active overlay state for geofence, POI and KML layers.

---
