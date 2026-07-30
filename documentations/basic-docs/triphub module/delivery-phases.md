## Delivery Phases

### Phase 1 — Core Web Planning

- Territory list/create/edit.
- Target list/create/edit/disable/delete.
- Haltpoint list/create/edit/link targets.
- Route list and empty state.
- Manual route creation.
- Service area setup.
- Route review.
- Target frequency-generated service requests.
- Route edit restrictions and route versioning guardrails.
- Foundational Route Type configuration required for route steps, service types, OTP/POD/proof behavior and mobile execution rules.

### Phase 2 — Trips and Monitoring

- Trip list and filters.
- Trip creation.
- Trip detail/info card.
- TripHub map view.
- Path replay.
- Hold, End and Re-run trip flows.
- Route deviation alert integration.
- Exception reassignment for Load Full, Breakdown and Skipped Target.

### Phase 3 — Workforce Mobile Execution and Exceptions

- Workforce mobile My Trips: Ongoing, Upcoming and History.
- Mobile trip cards, trip detail and route timeline.
- Start Trip with pre-trip checklist.
- Target/haltpoint execution states and proof capture.
- Mobile complete trip, hold trip and incomplete-target warning.
- Mobile adhoc request creation.
- Breakdown management and SOS integration.
- Call Admin and event audit.
- Command Log and event audit.

### Phase 4 — Configurability and Vertical Extensions

- Advanced Route Type configuration and vertical extensions.
- Target Type locking after TripHub activation.
- Dynamic target forms.
- Checklist/VCR framework.
- Attendance and break integration.
- School Transport/Bus993 parent visibility.
- Reporting pack.

### Phase 5 — Optimisation and Integrations

- Auto route optimisation improvements.
- External target/order sync.
- KML and geofence/territory automation.
- Advanced analytics and route performance scoring.


### Delivery sequencing notes

Phase sequencing should account for the following dependencies:

- Scheduler and Shift Master remain separate-module dependencies; TripHub should only consume their outputs and expose navigation/visibility touchpoints.
- Auto-routing field-level configuration should use user-filled inputs during route creation; backend must provide validation response, timeout handling and generation-result states.
- Manual-route haltpoint selection behavior should be locked before route builder engineering starts because it affects selection state, pagination, map selection and API contracts.
- Route Type configuration should be delivered before mobile execution rules because OTP, POD, FaceSync, adhoc and proof requirements depend on route-type configuration.
- Mobile breakdown, break, OTP, POD, cancellation and sync-failure states should not be pushed as visual-only screens; they need status/event models and recovery behavior.

---
