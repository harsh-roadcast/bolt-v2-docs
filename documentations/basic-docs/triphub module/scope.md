## Scope

### In scope

- TripHub navigation and entity structure.
- Territory management.
- Target management.
- Haltpoint management.
- Route list, empty state and route creation flows.
- Manual route creation.
- Auto route creation.
- Service area setup using manual drawing, existing geofence selection or KML upload.
- Route review, validation and scheduling state.
- TripHub integration touchpoints with the separate Scheduler / Shift Master module, limited to route schedule visibility, entry points and generated-trip consumption.
- Auto-routing field-level configuration, validation, generation states and routing strategies.
- Route-mode step matrix for Manual, Auto and Service Area route creation.
- Route empty-state matrix for Bin/Target and Haltpoint readiness states.
- Route edit, disable and versioning behavior.
- Trip list hierarchy, trip duplication, route/shift filters and create-trip-for-route behavior.
- Mobile OTP, POD, cancellation, adhoc photo capture, breakdown recovery, break handling, calling, forms, and sync/error states.
- Trip list, filters, status states and trip creation.
- Trip detail side panel / info card.
- TripHub map view.
- Path replay.
- Adhoc request and adhoc assignment.
- Hold, end and re-run trip flows.
- Configurable route types and service types as a platform rule framework.
- Route Type configuration for route creation rules, service-area behavior, service types and vehicle-assignment allowance.
- Target Attributes configuration with TripHub-specific dynamic fields and preview.
- Target Setup configuration for assigning target datasets/types to organisations.
- Admin-side TripHub Configuration landing page.
- Workforce, attendance, break, checklist, SOS and breakdown requirements as product capabilities.

Scheduler module boundary: TripHub includes only route-level schedule visibility, scheduler entry points, and generated-trip consumption. Shift Master, recurrence configuration, holiday handling, schedule exceptions, and missed-generation retry policy are owned by the connected Scheduler specification.
- Reporting and audit expectations.
- Business rules from TripHub Solution Documentation: target-type lock, attribute lifecycle, frequency-generated service requests, exchange handling, route-edit restrictions, adhoc route integrity, deviation alerts, exception reassignment and re-run behavior.

### Out of scope unless separately designed

- Full independent Workforce App functionality outside TripHub execution scope.
- Full Parent App / Bus993 mobile UX.
- Full platform-wide dynamic form-builder product beyond TripHub target-attribute configuration.
- Full HRMS / FaceSync API technical contract.
- Advanced route optimisation algorithm internals.
- Billing or add-on monetisation of TripHub.
- Public API documentation for external route/target sync.

---
