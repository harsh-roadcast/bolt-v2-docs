## Territory Management

Territories allow organisations to organise operational areas, service regions and route ownership. Territories may be used to scope which routes, haltpoints or service areas are available to a team.

Core requirements:

- Display territories in a list/table view.
- Support a two-level hierarchy for V1: Territory → Sub-territory.
- Allow creation of sub-territories under a parent territory only. Third-level nesting is future scope.
- Support linking routes to a territory.
- Support linking an existing geofence to a territory where applicable.
- Support KML-driven territory or service-area creation where approved by product.
- Prevent deletion or removal of a territory if active routes/trips depend on it.
- Child territory must remain logically under its parent unless explicitly moved.
- A route can belong to only one territory at a time.

Territory list columns should include at minimum: ID, Name, Sub Territory count, Linked Routes, Created On and Actions.

Action menu options should support View/Edit, Create Sub Territory and other admin-permitted actions.

![Territories list](../.gitbook/assets/territory-list.png)

*The Territories list exposes hierarchy, linked-route counts, filters, map/list switching, and row actions.*

![Create a territory](../.gitbook/assets/territory-create.png)

*Territory creation captures parent hierarchy, organisation scope, and spatial boundary information.*


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
