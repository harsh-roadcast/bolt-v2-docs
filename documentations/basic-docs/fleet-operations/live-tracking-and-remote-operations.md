---
description: >-
  The Live Tracking dashboard provides a real-time view of your entire fleet. It
  combines an interactive map with a dynamic vehicle list, allowing dispatchers
  to monitor status, location, and events ins
---

# Live Tracking & Remote Operations

### 1. The Dashboard Layout

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

When you click "Live Tracking" in the sidebar, you will see three main areas:

1. The Map (Right Pane): Displays vehicle icons, geofences, and Points of Interest (POIs).
2. The Sidebar (Left Pane): A searchable list of all assets, categorized by status.
3. The Detail Card (Bottom/Overlay): Appears when you select a specific vehicle.

***

### 2. Navigating the Map

The map is built for speed and clarity. You can customize what you see using the Layer Selector (usually top-right).

* Map Layers: Switch between `Default` (Street View), `Satellite`, or `Hybrid`.
* Traffic Layer: Toggle real-time traffic density (Green/Yellow/Red lines) to help route drivers around congestion.
* Clusters: To keep the map clean, vehicles close together are grouped into Clusters (colored circles with numbers).
  * _Action:_ Click a cluster to zoom in and see individual vehicles.

***

### 3. Vehicle Status & Icons

Vehicles are color-coded so you can understand their status at a glance.

| Color  | Status   | Definition                                                                 |
| ------ | -------- | -------------------------------------------------------------------------- |
| Green  | Running  | Engine is ON and vehicle is moving.                                        |
| Yellow | Idle     | Engine is ON but vehicle has been stationary for over 5 minutes.           |
| Red    | Stopped  | Engine is OFF.                                                             |
| Grey   | Inactive | Device has not reported data for more than 24 hours (No Signal/Power Cut). |

<figure><img src="../../.gitbook/assets/Frame 22.png" alt=""><figcaption></figcaption></figure>

### 4. Monitoring a Specific Vehicle

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

To track a single asset, find it in the sidebar list or click its icon on the map. This opens the Vehicle Detail Card, which displays:

* Live Metrics: Current Speed, Odometer, and Fuel Level.
* Location: Current address and time since last update.
* Sensors: (If equipped) Temperature, Door Status, or AC On/Off.

#### Available Actions

From the detail card, you can perform remote operations:

* 📍 Playback: View the route history for today or a custom date range.
* 🔗 Share Location: Generate a temporary public link to share the vehicle's location with a customer.
* 🛑 Immobilize: (Authorized Admins Only) Remotely cut off the engine in case of theft.

#### Vehicle Marker Legend & Status Logic

This page defines the visual indicators used on the Live Tracking map. Use this reference to understand fleet status at a glance.

**Vehicle Status Colors**

The system color-codes markers based on real-time telematics data received from the device hardware.

<table data-header-hidden><thead><tr><th width="132"></th><th width="123"></th><th width="226"></th><th></th></tr></thead><tbody><tr><td><strong>Status</strong></td><td><strong>Color</strong></td><td><strong>Hardware Condition</strong></td><td><strong>Logic</strong></td></tr><tr><td><strong>Moving</strong></td><td>Green</td><td>Ignition ON + Speed > 0</td><td>Vehicle is actively performing a trip.</td></tr><tr><td><strong>Idle</strong></td><td>Yellow</td><td>Ignition ON + Speed = 0</td><td>Engine is running but vehicle is stationary. High idling triggers "Fuel Waste" alerts.</td></tr><tr><td><strong>Parked</strong></td><td>Red</td><td>Ignition OFF</td><td>Vehicle is stationary and engine is shut down.</td></tr><tr><td><strong>Inactive</strong></td><td>Grey</td><td>No Data > 10 Mins</td><td>Device is unreachable. Check SIM data or power supply (See Troubleshooting).</td></tr></tbody></table>

**Vehicle Type Icons**

Bolt V2 utilizes distinct SVG icons to differentiate between asset classes.

<table data-header-hidden><thead><tr><th width="168"></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Asset Type</strong></td><td><strong>Icon Description</strong></td><td><strong>Primary Use Case</strong></td></tr><tr><td><strong>Car</strong></td><td>standard sedan silhouette</td><td>Passenger vehicles and executive fleet.</td></tr><tr><td><strong>Truck</strong></td><td>Heavy-duty logistics silhouette</td><td>Cargo transport and long-haul delivery.</td></tr><tr><td><strong>Bike</strong></td><td>Motorcycle/Scooter silhouette</td><td>Last-mile delivery and field agents.</td></tr><tr><td><strong>Ambulance</strong></td><td>Emergency vehicle with medical cross</td><td>Critical care and emergency response units.</td></tr><tr><td><strong>ID Card</strong></td><td>Person/Portable tag icon</td><td>Personal trackers or valuable package tracking.</td></tr></tbody></table>

#### Advanced Map Indicators

* **Directional Arrows:** When a vehicle is moving, a small arrow appears on the marker pointing in the direction of travel (Heading).
* **Clustering:** When zoomed out, multiple vehicles in close proximity group into a "Cluster Circle" showing the total count. Click the cluster to expand.
* **Immobilization Badge:** A "Lock" icon overlay appears if the **Remote Immobilization** command is active (Relay is cut).

#### Remote Commands (Immobilization)

<div data-full-width="true"><figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure></div>

For vehicles equipped with supported hardware, operators can send remote commands:

* **Immobilize:** Remotely disables the vehicle's starter relay. This is a critical security feature used in theft recovery.
* **Parking Mode:** Create a temporary "electronic lock" around a vehicle. If the vehicle moves while this is active, high-priority alerts are sent to the Command Center.

### 5. Managing Zones (Geofences & POIs)

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

The tracking screen also allows you to manage your virtual boundaries. Switch tabs in the left sidebar to view:

* Geofences: Polygonal zones (e.g., "Main Warehouse"). You will receive alerts when vehicles enter or exit these zones.
* POIs (Points of Interest): Specific markers for client locations or fuel stations.

#### Common Questions

Q: Why is a vehicle showing as "Grey/Inactive"? A: This usually means the GPS device has lost power or cellular network. Check if the vehicle is parked underground or if the device has been tampered with.

Q: How fast does the map update? A: The map refreshes automatically every 10-30 seconds depending on your device's configuration. You do not need to refresh the page.
