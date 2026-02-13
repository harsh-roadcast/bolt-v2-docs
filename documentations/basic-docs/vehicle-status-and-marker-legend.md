# Vehicle Status & Marker Legend

The Live Tracking map uses a comprehensive visual language to communicate the real-time status of your fleet at a glance. Understanding these color codes and icons is essential for quick decision-making and operational awareness.

#### 1. Vehicle Status Colors

Each vehicle marker on the map is color-coded based on its real-time telemetry data. This "Traffic Light" system allows you to instantly assess fleet activity.

| Status       | Color      | Hardware Condition              | Operational Meaning                                                                                                                       |
| ------------ | ---------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Moving**   | **Green**  | Ignition **ON** + Speed **> 0** | The vehicle is on an active trip and moving towards its destination.                                                                      |
| **Idle**     | **Yellow** | Ignition **ON** + Speed **= 0** | The engine is running, but the vehicle is stationary. Excessive idling may indicate traffic, loading/unloading, or fuel wastage.          |
| **Parked**   | **Red**    | Ignition **OFF**                | The vehicle is completely shut down. The engine is off, and it is parked at a location.                                                   |
| **Inactive** | **Grey**   | No Data > **10 Mins**           | The device has stopped communicating with the server. This could be due to a power cut, dead battery, or cellular network loss (No GPRS). |

<figure><img src="../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

#### 2. Vehicle Type Icons

Bolt V2 differentiates assets not just by status, but by type. The system renders distinct SVG silhouettes for various asset classes to help dispatchers distinguish between resources.

* **Car:** Standard sedan silhouette.
* **Truck:** Heavy-duty logistics vehicle profile.
* **Bike:** Motorcycle icon for last-mile delivery.
* **Ambulance:** Emergency vehicle marked with a medical cross.
* **ID Card:** Used for personal trackers or high-value cargo tags (non-vehicular).

#### 3. Advanced Status Indicators

Beyond the basic color, the marker itself can display badges to indicate critical alerts or configurations.

**3.1 Immobilization Badge**

* **Symbol:** A small **Lock Icon** overlaying the vehicle marker.
* **Meaning:** The vehicle's starter relay has been remotely cut via the "Immobilize" command. The driver will not be able to restart the engine until it is unlocked.

**3.2 Alert Pulsing**

* **Visual:** The marker radiates a concentric "Pulse" animation.
* **Meaning:** A high-priority alert (SOS/Panic Button, Crash Detection, or Geofence Breach) has been triggered within the last minute.

#### 4. Logic Flow: Status Determination

The system follows a strict hierarchy to determine which color to display. "Inactive" status always takes precedence over ignition data to ensure you know when data is stale.

```mermaid
graph TD
    Data[Telemetry Packet Received] --> TimeCheck{"Last Update < 10 Mins?"}
    TimeCheck -- No --> Inactive["Status: GREY (Inactive)"]
    TimeCheck -- Yes --> Ignition{"Ignition ON?"}
    Ignition -- No --> Parked["Status: RED (Parked)"]
    Ignition -- Yes --> Speed{"Speed > 0?"}
    Speed -- No --> Idle["Status: YELLOW (Idle)"]
    Speed -- Yes --> Moving["Status: GREEN (Moving)"]

    Inactive --> Render[Render Marker]
    Parked --> Render
    Idle --> Render
    Moving --> Render
```

#### 5. Troubleshooting Status Issues

| Symptom                                 | Likely Cause       | Resolution                                                                                      |
| --------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------- |
| **Marker stuck on "Moving"**            | GPS Latch / Freeze | The device may have lost GPS fix while moving. Check the "Satellites" count in the sensor card. |
| **Vehicle is running but shows "Grey"** | Network Blindspot  | The vehicle is in a basement or tunnel. Data will "burst" upload once connectivity is restored. |
| **"Idle" for hours**                    | Driver Behavior    | Driver may be sleeping with AC on. Check "Fuel Consumption" to verify waste.                    |
