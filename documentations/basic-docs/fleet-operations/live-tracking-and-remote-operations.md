# Live Tracking & Remote Operations

#### Live Tracking & Remote Operations

The tracking interface utilizes **Leaflet** to provide a high-performance, real-time visualization of your fleet.

* **Visual Overlays:** Toggle between standard road maps, high-resolution satellite imagery, and live traffic data.
* **Marker Logic:** Vehicle icons change color dynamically based on state:
  * **Green:** Ignition On / Moving.
  * **Yellow:** Idle (Ignition On but stationary).
  * **Red:** Ignition Off.
  * **Grey:** Inactive (No data received for a set period).

<figure><img src="../../.gitbook/assets/Frame 22.png" alt=""><figcaption></figcaption></figure>

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

For vehicles equipped with supported hardware, operators can send remote commands:

* **Immobilize:** Remotely disables the vehicle's starter relay. This is a critical security feature used in theft recovery.
* **Parking Mode:** Create a temporary "electronic lock" around a vehicle. If the vehicle moves while this is active, high-priority alerts are sent to the Command Center.

#### Managing Geofences & POIs

* **Geofences:** Draw virtual boundaries (Circles or Polygons). Configure alerts for entry, exit, or stay-duration.
* **Points of Interest (POI):** Mark regular destinations like gas stations, warehouses, or customer offices.
