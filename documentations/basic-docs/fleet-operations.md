---
description: >-
  The Fleet Operations module allows you to onboard new vehicles, manage driver
  profiles, and organize your fleet into logical groups. Unlike "Live Tracking"
  (which is for monitoring), this area is for
---

# Fleet Operations

### 1. Vehicle Management

To view your fleet list, navigate to Management Hub > Vehicles in the sidebar.

#### The Vehicle List

The main table displays all assets currently active in your account.

* Search: Use the top bar to find vehicles by Registration Number, IMEI, or Driver Name.
* Filters: Filter by `Status` (Active/Inactive) or `Group`.
* Actions:
  * ✏️ Edit: Update vehicle details (e.g., Change Model, Update Registration).
  * 🔗 Link Device: Assign a new GPS tracker (IMEI) to an existing vehicle profile.
  * 🗑️ Deactivate: Remove a vehicle from your subscription (stops billing).

#### Adding a New Vehicle

1. Click the "+ Add Vehicle" button.
2. Step 1: Device Setup
   * Enter the IMEI (15-digit serial number) of your GPS device.
   * Select the Device Model from the dropdown.
3. Step 2: Vehicle Details
   * Enter the Registration Number (License Plate).
   * Select Vehicle Type (Truck, Car, Bike, etc.) for correct icon representation on the map.
4. Step 3: Assignment
   * (Optional) Assign a Driver immediately.
   * Select a Group (e.g., "North Zone") to ensure the right managers can see it.

***

### 2. Driver Management

Navigate to Management Hub > Drivers to maintain a digital database of your staff.

#### Creating a Driver Profile

1. Click "Add Driver".
2. Personal Details: Name, Phone Number (used for login if enabled), and Employee ID.
3. License Info: Upload a photo of the Driving License and enter the expiry date.
   * _Note: The system can trigger alerts when a license is nearing expiry._
4. RFID/iButton: If your vehicles use Driver ID sensors, enter the tag ID here to auto-assign drivers to trips.

#### Assigning Drivers to Vehicles

* Manual Assignment: Go to the Vehicle List, click "Edit", and select a driver.
* Auto-Assignment: If using RFID tags, the driver is automatically assigned to the vehicle when they swipe their card in the cabin.

***

### 3. Grouping & Organization

Groups allow you to segment your fleet so that specific managers only see relevant vehicles.

* Navigate to: Settings > Device Groups.
* Create Group: Name it (e.g., "Heavy Haulage" or "Mumbai Branch").
* Assign Assets: Select multiple vehicles and move them into the group.
* Permissions: When inviting a new Sub-User (Dispatcher), you can restrict their view to _only_ specific groups.

***

### 4. Maintenance & Documents

Keep your fleet compliant by uploading digital records.

#### Document Locker

For every vehicle or driver, you can upload:

* RC (Registration Certificate)
* Insurance Papers
* PUC (Pollution Certificate)
* Permits

To Upload:

1. Select the Vehicle/Driver.
2. Go to the "Documents" tab.
3. Click "Upload" and set an Expiry Date.
   * _Benefit:_ Bolt V2 will send you a reminder notification 30 days before any document expires.

***

#### Frequently Asked Questions

Q: I added a vehicle, but it's not on the map. A: Ensure the device is powered on and has a valid SIM card. New devices may take up to 15 minutes to sync for the first time.

Q: Can one vehicle belong to multiple groups? A: No, a vehicle can typically belong to only one primary reporting group to prevent permission conflicts.

Q: How do I swap a GPS device from one truck to another? A: Go to Vehicle > Edit > Unlink Device. Then, go to the new vehicle and select Link Device, entering the same IMEI.
