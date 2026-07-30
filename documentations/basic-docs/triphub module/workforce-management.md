## Workforce Management

TripHub should support workforce assignment at trip level.

Supported workforce types:

- Driver.
- Helper.
- Attendee.
- Inspector.
- Field Agent.

A trip may have:

- One primary driver.
- Multiple helpers if route type allows.
- Multiple attendees if route type allows.
- Optional inspector/field agent if the route type is survey or service based.

Rules:

- Driver may be mandatory for executable trips.
- Helper/attendee requirements are route-type configurable.
- Workforce conflicts should be flagged when the same employee is assigned to overlapping trips.
- Workforce status should show attendance state when HRMS integration is active.

---
