---
layout:
  width: wide
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# TripHub & Waste Management

Welcome to TripHub. This platform helps you manage waste collection operations efficiently. It allows you to plan routes, track vehicles in real-time, and handle unexpected pickups (like bulky waste) without messing up your long-term schedules.

### 1. Getting Started: Setting Up Targets

Before you can send out trucks, you need to define what needs to be picked up. In TripHub, we call these Targets.

#### What is a Target?

A Target is simply a bin or a collection point.

* Details: Each target has a name, address, and specific GPS coordinates.
* Frequency: You can set how often a bin needs to be picked up. If you set the frequency to more than 1, the system automatically creates duplicate requests for you.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

#### How to Create a Target

1. Navigate to the Target Lists menu.
2. Click the Create Target button.
3. Enter the waste type, bin size, and load capacity.
4. Save your target.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

### 2. Organizing Locations: Halt Points

To make routing efficient, we group nearby bins into Halt Points.

#### What is a Halt Point?

A Halt Point is a specific location where the truck stops. A single halt point can handle multiple bins (Targets) within a specific radius.

* Geo-Fencing: You define a radius (area covered) to ensure the driver is at the right spot.
* Linked Targets: You can link multiple bins to one stop.

<figure><img src="../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

### 3. Planning Your Routes

A Route is your master plan. It is a fixed sequence of Halt Points that your trucks will follow.

#### Creating a Manual Route

1. Select the Manual Route option.
2. Choose the Halt Points you want to service.
3. The system will calculate the Total Distance and Estimated Time for you.

Important Rules:

* No Adding New Targets: You cannot add a completely new target to an active route. You must create a new route if you need to add a new stop.
* Exchange Service: If you are swapping a bin (Exchange), you must add a corresponding "Drop" location to the route.

<figure><img src="../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

### 4. Daily Operations: Trips

A Trip is the actual execution of a route on a specific day. This is where you assign a driver and a vehicle.

#### Dispatching a Trip

* Assign Resources: Select a vehicle and a driver for the route.
* Status Tracking: Monitor the trip status as it changes from _Assigned_ to _In Progress_, _Breakdown_, or _Completed_.

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### Real-Time Monitoring

Use the dashboard to see exactly where your vehicles are. You can compare the Planned vs Actual timings to check for delays.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### 5. Automating Operations: Route Scheduler

Instead of creating trips manually every day, you can use the Route Scheduler to plan your operations for the entire month (or longer).

How it works: You define the schedule once. When the scheduled time arrives, the system automatically creates the trip for that route, assigning the correct vehicle and driver without you needing to lift a finger.

#### The Scheduler Dashboard

The Scheduler gives you a calendar view of all your planned routes. You can see which routes are active and which days have shifts assigned.

1. Navigate to Scheduler -> Shift Master.
2. You will see a grid view showing dates and assigned routes.

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

#### Creating a Custom Shift

To set up a schedule, you create a "Shift". This tells the system which route to run and when.

1. Click on Create Route.
2. Select Custom Shift.
3. Select Route: Choose the Master Route you want to schedule.
4. Shift Name: Give it a clear name (e.g., "Morning Collection Zone A").
5. Time: Set the Start Time and End Time for the shift.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

#### Setting Recurring Schedules

You usually don't want to schedule just one day. You want the route to run every Monday, Wednesday, and Friday, for example.

1. Scroll down to the Schedule Shift checkbox.
2. Select how often it repeats (e.g., Repeat Every 1 Week).
3. Click the specific days (M, T, W, Th, F, Sa, Su) to activate them.
4. Set an Ends date if you want the schedule to stop after a certain time (or leave it as "Never").

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### Assigning Resources (Vehicle & Driver)

For the automation to work fully, you must tell the system who is driving.

1. Under Additional Info, select the Vehicle that will handle this route.
2. Select the Driver.
3. (Optional) Set Threshold Times for idle alerts.
4. Click Save Shift.

_Note: When the scheduled time occurs, the system will generate a live Trip with these exact details._

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

### 6. Handling Unexpected Waste (Ad-Hoc)

Sometimes you need to collect Bulky Waste or handle a request that isn't on the regular schedule. TripHub handles this without breaking your master routes.

#### How Ad-Hoc Works

1. Create Request: A driver can raise a request from the app, or a manager can create one in the portal.
2. Assign: You assign this extra task to an existing trip.
3. Execute: The driver performs the pickup.
4. Auto-Restore: Once the trip is done, the master route returns to normal. The extra stop is not permanently added to the route.

{% columns %}
{% column %}
<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}



### 7. The Driver App

The mobile app is the driver's main tool for attendance and navigation.

#### Key Features for Drivers

* Face Sync Attendance: Drivers check in and out using facial recognition with geofence validation.
* Navigation: Live visuals of the route integrated with Google Maps.
* Proof of Delivery (POD): Drivers must capture a photo of the bin to confirm the job is done.
* Vehicle Breakdown: Drivers can report a breakdown directly from the app.

{% columns %}
{% column %}
<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
<figure><img src="../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
<figure><img src="../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}



<figure><img src="../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

### 8. Hardware & Reports

TripHub connects with smart hardware to keep your fleet safe and efficient.

#### Supported Hardware

* AI Dash Camera: A 3-channel camera that detects lane departures, smoking, and phone usage to keep drivers safe.
* Fuel Sensors: Bluetooth sensors (Escort TD BLE) that monitor fuel levels with high precision ($$\le 1\%$$ error) to prevent theft.
* OBD Tracker: The Teltonika FMC003 plugs into the vehicle to read real odometer and fuel data.

{% columns %}
{% column %}
<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>


{% endcolumn %}

{% column %}
<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>


{% endcolumn %}

{% column %}
<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>


{% endcolumn %}
{% endcolumns %}

#### Reporting

You can generate custom reports to audit operations, including:

* Missed Bin Detection.
* Driver Attendance.
* Trip Summaries.

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

