## 7. Information Architecture

The Video Monitoring module should contain two primary navigation entries:

1. **Command Center**
   - Live stream grid.
   - Stream controls.
   - Search, sort, filters and favourites.
   - AI Insights panel.
   - Fleet distribution and stream/device status.
   - Actions: snapshot, recording, call, map, history, incident-centric view.

2. **PAP Incidents**
   - Recent incidents.
   - View all incidents.
   - Severity metrics.
   - Incident cards.
   - Incident detail.
   - Incident heat-map and hotspots.
   - Event reference guide.

Supporting workflows are opened from these pages:

- Device History.
- View on Map.
- Incident Details.
- Evidence download.
- Incident-centric live stream view.

```mermaid
flowchart TD
    A[Video Monitoring] --> B[Command Center]
    A --> C[PAP Incidents]
    B --> D[Live Stream Grid]
    B --> E[AI Insights]
    B --> F[Device History]
    B --> G[View on Map]
    B --> H[Call Device]
    C --> I[Recent Incidents]
    C --> J[View All Incidents]
    C --> K[Incident Detail]
    C --> L[Heat-map and Hotspots]
    K --> M[Evidence Video]
    K --> N[Incident Location]
```

---
