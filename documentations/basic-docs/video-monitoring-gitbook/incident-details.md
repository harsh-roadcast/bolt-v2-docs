## 16. Incident Details

Incident Details is the investigation page for one incident.

![Incident Details](../../.gitbook/assets/incident_details.png)

*Incident investigation page with evidence playback, incident metadata and map location.*

### 16.1 Page Content

The page should show:

- Back link to PAP Incidents or originating context.
- Evidence video player.
- Incident metadata.
- Incident location section.

### 16.2 Incident Metadata

The incident information should include:

- Incident name.
- Device ID / IMEI.
- Group name.
- Vehicle number.
- Severity.
- Incident time.
- Event name.
- Channel name.
- Device model.
- Driver name, if available.
- User name, if available.
- Location coordinates and address where available.

### 16.3 Video Player Actions

The current interface shows video controls and menu actions including:

- Download.
- Playback speed.
- Picture-in-picture.
- Fullscreen.

Rules:

- Video should load from the evidence clip associated with the incident.
- Download action requires permission.
- If the clip is unavailable, show a clear unavailable state and keep the metadata visible.
- Player actions should not change the incident verification status unless a separate verification workflow is introduced.

### 16.4 Incident Location

The `Location of Incident` area should show a map or location context for the incident.

Rules:

- If coordinates are available, show map focus.
- If only address is available, show address text.
- If no location exists, show `Location unavailable` rather than leaving the section blank.

---
