## Information Architecture

TripHub web should be organised around the following primary sections:

- **Territories** — create, view, edit and organise operating territories or service zones.
- **Targets** — create and manage atomic service points such as bins, students, customers or assets.
- **Haltpoints** — create stops that group targets and become route building blocks.
- **Routes** — create and maintain route definitions using manual, auto-route or service-area methods.
- **Trips** — create executable trip instances, assign resources, monitor status and handle exceptions.
- **Map View** — view trip/route/entity execution spatially.
- **Reports** — review performance, compliance and exceptions.
- **Configuration** — Super Admin / Admin-side configuration for TripHub Target Setup, Target Attributes, Route Types, dynamic target forms and operational rules.

The list screens should follow a consistent table pattern with Create, Download Report, Filters, search, view switcher and row action menus.


### Territory hierarchy, boundary and deletion behavior

Additional operational requirements:

- Expanded territory view must show sub-territories and assigned routes.
- Creating a sub-territory requires parent territory selection.
- Territory creation must support either selecting an existing geofence or uploading KML to create and link a new geofence/boundary.
- Territory boundary management must support edit, replace and unlink behavior, subject to dependency checks.
- Territory filters must include organisation, created date, route type and territory where applicable.
- Delete must show a confirmation modal and must be blocked if linked routes, active schedules or future trips depend on the territory.
- The system must prevent hierarchy cycles, such as making a parent territory a child of its own descendant.
- V1 maximum territory hierarchy depth is two levels: Territory → Sub-territory. A third level is future scope.
- Parent change should require dependency validation and should not silently move linked routes, users or geofences unless inheritance is explicitly supported.
- Overlapping territory boundaries should either be allowed with warnings or blocked by route-type configuration. This remains an open product decision.
- Child territories must not automatically inherit routes, users or geofences from the parent unless inheritance is explicitly configured.
