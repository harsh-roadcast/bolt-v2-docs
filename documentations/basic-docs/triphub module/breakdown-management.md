## Breakdown Management

Breakdown is a first-class trip status and exception.

Driver can mark a trip as Breakdown from Workforce App. Admin/supervisor should be able to view and resolve it from web.

![Mobile breakdown action](../.gitbook/assets/mobile-breakdown.png)

*The driver can report a breakdown from the active trip surface while retaining trip and location context.*

System actions:

- Create Breakdown event.
- Send notification.
- Update trip status to Breakdown.
- Record affected vehicle, driver, timestamp, location and reason.
- Show breakdown status on trip list/detail.

Admin actions:

- Change Driver.
- Change Vehicle.
- Change both Driver and Vehicle.
- Resume Trip after reassignment.
- End Trip if operation cannot continue.

### Mobile breakdown confirmation behavior

The Workforce mobile design includes Report Vehicle Breakdown and Confirm Breakdown. A confirmed breakdown should create the event, update trip status, notify web users and preserve the driver's last known location.

Rules:

- Newly assigned driver should receive Resume Trip, not Start Trip.
- Upon resume, status changes from Breakdown to In Progress.
- Historical timeline must show the breakdown segment and resource reassignment.


### Mobile breakdown recovery flow

The mobile breakdown flow must capture whether the vehicle can move.

Rules:

- When breakdown is reported, a Breakdown event is created and the Trip status changes to Breakdown. This is separate from the On Hold status, which is used only for manual/admin hold flows.
- Driver must specify whether the vehicle can move.
- Can-move case: driver waits for admin action and may receive Mark Vehicle Ready / Resume flow once approved.
- Cannot-move case: system shows replacement vehicle en route, ETA and replacement driver information where assigned.
- Replacement vehicle handover may require number-plate scan.
- Confirm Replacement Vehicle Received must validate expected vehicle/number plate.
- Incorrect number-plate error must block confirmation and allow retry or Contact Admin.
- Contact Admin should be available during recovery.
- Resume rules must define whether the same driver continues, replacement driver continues or admin reassigns the remaining targets.
- Breakdown timeline must store report, replacement assignment, vehicle received, resume and completion events.

---
