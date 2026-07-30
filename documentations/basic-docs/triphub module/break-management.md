## Break Management

Workforce App should support break tracking.

![Mobile break state](../.gitbook/assets/mobile-break.png)

*The active break state displays trip context, remaining break time, and the action to resume work.*

Actions:

- Break Start.
- Break End.

Data should be stored in HRMS or the workforce service depending on final architecture.

TripHub web should display:

- Break count.
- Total break duration.
- Break timeline.
- Break start/end location where available.
- Break compliance state if route type defines allowed break duration.


### Mobile break states and policy

Breaks must support both mandatory and flexible patterns where configured.

Requirements:

- Mandatory breaks should be shown when the route/shift requires a break window.
- Flexible breaks should be available only when the driver has remaining break quota.
- Fixed break windows must show available/not-available states.
- Remaining break quota and countdown must be visible during active break.
- End Break must return the driver to active trip execution when allowed.
- Early break, late break and overrun handling must be defined by route/shift policy.
- Break start/end must store trip ID, driver ID, route ID, start time, end time, duration, location and policy outcome.
- If break starts while navigation/target service is active, the app must pause or block target completion based on policy.

---
