## Target Management

Targets are the atomic service points used by TripHub. The same underlying entity should support different business labels such as Bin, Student, Customer, Asset, Order Stop or Inspection Site depending on Route Type.

### Target list

The target list should support:

- Table view with pagination.
- Create Target / Create Bin / Create Student label based on route type context.
- Download Report.
- Search.
- Filters.
- View switcher where map/list variants are available.
- Row actions.
- Expanded table state for larger column sets.

![Targets list](../.gitbook/assets/target-list.png)

*The target table combines system fields with organisation-specific attributes and supports list or map-based operations.*

Standard system columns:

- Target ID
- Target Name
- Target Type
- Organisation
- Linked Territory where applicable
- Linked Haltpoint
- Location / Coordinates
- Address
- Owner / Linked Users where user-target mapping is enabled
- Status
- Created On
- Last Updated On
- Actions

Configured / vertical-specific target attributes:

- Load, waste type, bin size, school class/section, order temperature, mode of payment, OTP, order total, estimated reach time, estimated travel distance, proof of delivery and similar fields must not be treated as universal Target columns.
- These fields should be rendered only when they are part of the configured Target Type, Route Type, vertical template or target attribute schema.
- Target tables must support schema-driven columns so that Bin, Student, Customer, Employee, Order and Field-Service use cases can show different operational fields without hard-coding a universal table model.

Default system-defined target fields from TripHub Solution Documentation should include:

- External ID
- Name
- Address
- Latitude / Longitude
- Load (kg)
- Frequency

Frequency rules:

- Frequency defaults to `1`.
- Frequency defines how many times a target must be serviced in a route/trip cycle.
- If Frequency is greater than `1`, TripHub must generate duplicate service requests for the same target during route planning.
- The first service request follows the normal planned sequence.
- Additional frequency-generated service requests should be placed at the end of the route by default, unless the route optimisation service explicitly repositions them and shows the result in route review.
- Frequency-generated duplicates are service requests, not separate target master records.

School-transport target columns may include Class, Section and Linked User instead of load/owner fields.

### Target creation

Target creation should support:

![Create a target](../.gitbook/assets/target-create.png)

*Target creation renders the system and configured fields that apply to the selected target type.*

- Manual form creation.
- Dynamic fields based on route type or target type.
- Location capture using address and/or latitude-longitude.
- Bulk CSV upload.
- Fetch from Database where enabled.
- Optional API/database sync in future phases.
- Optional auto haltpoint creation where configured.
- Optional automatic haltpoint linking where configured.
- Frequency/service schedule configuration for recurring operations.
- Waste type, bin size, service type, proof requirements and other vertical-specific attributes as configured.
- Target attribute fields configured in Admin should be rendered in this form for the selected organisation and target type.
- Admin-configured mandatory fields, validation rules, helper text and tooltip copy must be respected during create and edit.

### Target edit, disable and delete

- Edit should update the active target master record and should not mutate already-started or completed trip execution snapshots.
- Disable should prevent future route/trip selection but should not affect ongoing trips.
- Delete is supported as a permanent delete action for V1 and must be permission-gated.
- Permanent delete must show a strong confirmation dialog before execution.
- If a target is already referenced by active or future operational work, the UI must show the dependency impact before allowing deletion.
- Default Target actions are View, Edit, Disable, Delete and View Report where permitted.
- Device actions such as Send GPS Command, Share Location, Troubleshoot, Change IMEI, Immobilise or Live Stream must not appear as default Target requirements. They may appear only as conditional device-linked extensions when the target is explicitly linked to a device, vehicle or IoT asset and the action is enabled by entity type, permission and module configuration.


### Target import, user visibility and dependency behavior

Additional target requirements:

- Target import must support Upload via KML where the route type and target type allow spatial target ingestion.
- Link-user behavior must distinguish between targets visible to all permitted users and targets visible only to selected users.
- Target list must include a Linked Users column where user-target mapping is enabled.
- Target creation must support auto-create haltpoint at the same location when configured, as well as manual selection of an existing haltpoint.
- Exact filters should include organisation, created date/time, target type and owner/linked user.
- Disable must unlink the target from future route planning and future haltpoint/route selection where required, but ongoing trips must remain unchanged.
- Target data shown in tables must be schema-driven from configured attributes and vertical context, not a fixed universal column set.
- Device actions shown in shared table components must not become target requirements unless the target is explicitly device-linked.
