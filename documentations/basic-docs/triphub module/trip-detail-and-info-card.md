## Trip Detail and Info Card

Trip detail should be accessible from the trip table and map. The right-side detail panel/info card should provide operational context without losing the map/list context.

![Trip detail panel](../.gitbook/assets/trip-detail-panel.png)

*The detail panel keeps the Trip List visible while exposing the selected trip’s progress, route, timings, assignment, and actions.*

Supported detail tabs:

- Overview
- Trip Path / Route Path
- Linked Data
- Command Log

Overview should show:

- Route Name.
- Route or Trip Route Status.
- Completed/missed progress.
- Start/end and actual start/end time.
- Vehicle and driver information.
- Haltpoint/target counts.
- Latest update.

Trip Path should show:

- Sequenced haltpoints.
- Target IDs under haltpoints.
- Timestamps where available.
- Completed/missed/remaining state.
- Previous/Next navigation for trip path elements.

Linked Data should show dependent entities such as linked haltpoints, linked targets, documents, route metadata and other configured attributes.

Command Log should show system/user actions with timestamp, actor, command type and result.
