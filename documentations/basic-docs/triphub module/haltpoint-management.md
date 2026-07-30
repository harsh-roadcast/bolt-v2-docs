## Haltpoint Management

A Haltpoint is an operational stop that can group one or more targets. For waste collection, a haltpoint may represent a collection stop containing multiple bins. For school transport, a haltpoint may represent a pickup/drop location for multiple students. For logistics, it may represent a delivery cluster or customer stop.

Core requirements:

- Display haltpoints in a list/table view.
- Create haltpoints manually.
- Link and unlink targets.
- Support location, radius/area coverage and linked target count.
- Support edit flow and row actions.
- Support geo-based target linking: user can define a point/radius or service area and the system can suggest eligible targets inside the area.
- Allow manual add/remove from detected target candidates.
- Maintain haltpoint dependency rules when a route already uses the haltpoint.

Haltpoint list columns should include at minimum: ID, Name, Area Covered, Organisation, Linked Targets, Location, Created On, Last Updated On and Actions.

![Haltpoints list](../.gitbook/assets/haltpoint-list.png)

*The Haltpoints list shows operational stops and their linked-target context.*

![Create a haltpoint](../.gitbook/assets/haltpoint-create.png)

*Haltpoint creation supports location, radius, organisation, geofence controls, and target linking.*


### Haltpoint filters, detail panel and disable behavior

Additional haltpoint requirements:

- Haltpoint filters must include organisation, created date, route linkage, territory, geofence and Show Only Hub.
- Haltpoint detail panel must support Previous/Next navigation, area/radius, address, coordinates and linked target list.
- Create Haltpoint fields must include ID, Name, Radius/Area Covered, latitude, longitude, address, organisation, geofence alert configuration and linked targets.
- Disable must remove the haltpoint from future route/trip selection, subject to dependency checks, while active or completed trips retain their historical haltpoint snapshot.
- Haltpoint columns must be driven by target type, configured attributes and vertical context rather than treated as a fixed universal table model.
- Delete is supported as a permanent delete action for V1 and must be permission-gated. If a haltpoint is referenced by active, scheduled or future operational work, the UI must show the dependency impact before allowing deletion. Already-started or completed trip execution snapshots must remain readable through stored trip data.
