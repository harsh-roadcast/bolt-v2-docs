## Core Concepts

| Entity | Description | Key relationships |
|---|---|---|
| Territory | Operational area used to group routes, geofences, service zones or sub-territories. | Can contain child territories and linked routes. |
| Target | Atomic service point such as bin, student, customer, asset, delivery point or inspection point. | Can be linked to haltpoints and users. |
| Target Setup | Admin configuration that controls which TripHub target datasets/types are available for selected organisations. | Drives Target list availability, route creation eligibility and organisation-scoped TripHub setup. |
| Target Attribute Set | Admin-managed dynamic field schema for a target type such as Bin, School, Trip, Employee or Customer. | Drives web target forms, mobile forms where applicable, preview, validation and reporting columns. |
| Route Type Configuration | Admin-managed rule set defining how a route type behaves. | Drives route creation steps, haltpoint selection, service-area behavior, service types and vehicle assignment rules. |
| Haltpoint | Operational stop grouping one or more targets. | Used as building block of routes. |
| Route | Ordered or area-based collection of haltpoints/service areas. | Can be scheduled, edited, reviewed and used to create trips. |
| Shift | Scheduler-owned operational time window used by scheduled routes and generated trips. | TripHub displays shift names/statuses and passes route context to Scheduler. |
| Route Schedule | Scheduler-owned schedule definition that generates TripHub trip instances. | TripHub stores/receives schedule references and shows schedule state on routes/trips. |
| Recurrence Rule | Scheduler-owned repeat pattern for trip generation. | TripHub consumes generated trip instances and displays generation status/errors where relevant. |
| Route Version | Immutable route snapshot created when route edits affect execution logic. | Generated future trips should update to the latest route version until the trip is started; ongoing/completed trips retain the route version used at start/execution. |
| Trip | Executable instance of a route at a specific time with assigned vehicle/workforce. | Tracks live execution, progress and exceptions. |
| Service Area | Geographic area/path used to restrict or guide route execution. | Can be drawn, selected from geofence or imported from KML. |
| Workforce | Driver, helper, attendee, inspector or field agent assigned to execute work. | Linked to trip and attendance. |
| Vehicle | Assigned vehicle/device used to execute the trip. | Linked to map tracking and trip telemetry. |
| Adhoc Request | Unplanned service request created during execution. | Can be assigned to existing trip, new trip or pending queue. |
| Checklist | Configurable inspection/compliance form. | Can be required by route type or trip. |
| Attendance | Workforce presence/break state. | Pulled from HRMS/FaceSync/manual sources. |

### Dynamic terminology and business model configuration

TripHub is one configurable solution that can support multiple operating models such as Cab Operations, School Bus Operations, Waste Management Operations, Order Management System, Employee Transportation and Field Service. The underlying data model should remain stable, while user-facing labels, forms, table columns, mobile actions and reports adapt based on Admin-configured **Target Type**, **Target Attributes** and **Route Type**.

Examples:

| Operating model | Admin target type / terminology | Typical user-facing labels |
|---|---|---|
| Waste Management | `Target_Bin` | Bin, Waste Type, Load, Service Area, Pick/Drop/Exchange |
| School Bus Operations | `Target_School` / Student | Student, Guardian, Pickup, Drop, No Show, Boarding/Deboarding |
| Cab / Employee Transport | `Target_Employee` | Employee, Rider, Pickup Point, Drop Point, Shift |
| Order Management System | `Target_Customer` / Order | Customer, Order, Delivery Point, POD, OTP, Payment Mode |
| Field Service / Survey | `Target_Customer` / Site | Customer, Site, Job Location, Checklist, Photo Proof |

Rules:

- Approved product flows define the screen structure and visible interactions.
- Admin configuration controls terminology and available fields across web, mobile, reports, and exports.
- Labels such as Target, Bin, Student, Customer, Order, Haltpoint, Stop, Pickup, Drop, Completed, Missed and No Show must be rendered from configuration wherever the UI surface supports dynamic terminology.
- Reports and exports should use the same configured terminology shown in web and mobile surfaces.

---
