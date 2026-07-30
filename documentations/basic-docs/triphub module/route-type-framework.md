## Route Type Framework

TripHub must support configurable Route Types. A Route Type defines execution rules, labels, required entities, compliance requirements and service behavior.

Examples:

| Route Type | Target label | Primary behavior | Special rules |
|---|---|---|---|
| Waste Collection | Bin / Target | Pickup service across assigned territory or service area. | Adhoc target creation may be allowed; service area may be mandatory. |
| School Transport | Student | Pickup and drop tracking. | Guardian mapping, attendance, parent visibility and boarding/deboarding workflows. |
| Logistics | Customer / Order / Stop | Pickup, drop and exchange execution. | Proof of delivery and service type required. |
| Survey / Inspection | Site / Asset | Form-based execution. | Checklist and photo proof may be mandatory. |
| Employee Transport | Employee / Stop | Scheduled transport trips. | Attendee assignment and driver attendance validation. |
| Field Service | Customer / Asset | Task/service workflow. | Form, signature or issue capture may be mandatory. |

Route Type configuration should be available only to Super Admin or an equivalent product-admin role.

Configuration categories:

- Route behaviour: predefined targets, geofence-based route, dynamic route, route optimisation.
- Service types: pickup, drop, exchange.
- Workforce rules: driver required, helper required, attendee allowed, multiple attendees allowed.
- Adhoc rules: allow adhoc requests, save adhoc target, proof before/after service.
- Compliance rules: attendance mandatory, checklist mandatory, break tracking enabled, SOS enabled.
- Completion rules: OTP required, POD photo/signature/notes required, before/after proof, FaceSync checkpoints and exception reasons.
- Visibility rules: parent visibility, supervisor visibility, user-target mapping.
