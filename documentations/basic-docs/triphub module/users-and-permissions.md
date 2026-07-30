## Users and Permissions

| User type | Primary responsibilities | Access expectations |
|---|---|---|
| Super Admin | Configure route types, service types, target schemas, compliance rules and organisation-level TripHub capabilities. | Full configuration and admin access. |
| Organisation Admin | Manage targets, haltpoints, territories, routes, trips, workforce assignment and reports. | Full TripHub access within assigned organisation hierarchy. |
| Dispatcher / Operations Manager | Create routes/trips, assign vehicle/driver, monitor execution, manage adhoc requests and review exceptions. | Create, edit, assign, monitor and export permissions. |
| Supervisor | Monitor route/trip progress, handle exceptions, approve changes and assign adhoc work. | Operational monitoring and limited edit permissions. |
| Driver / Field Agent | Execute trips on Workforce App, mark target complete, upload proof, start/end breaks, raise SOS or breakdown. | Mobile execution permissions only. |
| Helper / Attendee | Participate in trip execution, attendance, checklists and service activities. | Mobile or attendance-linked permissions as configured. |
| Parent / Guardian | View linked student trip status, bus location and pickup/drop state. | Restricted to linked students and assigned trips. |
| Read-only User | Audit or view operational data. | View-only access to configured entities and reports. |

Permission rules:

- Users must only see entities within their assigned organisation hierarchy and user-target mapping scope.
- Route type configuration is Super Admin controlled.
- Create, edit, delete, disable, end trip, re-run, route schedule, export and command actions must be permission-gated.
- Sensitive operational actions such as ending a trip, re-running a trip, disabling a target, deleting a target or changing assigned resources must be audit logged.

### Permission action matrix

Final roles should not be hard-coded. TripHub permissions should be implemented as entity/action permissions that can later be mapped to organisation roles.

| Entity | View | Create | Edit | Disable | Delete | Assign | Schedule | Hold | End | Re-run | Export | Approve Adhoc | Override |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Territory | Yes | Yes | Yes | Yes | Yes, permission-gated | NA | NA | NA | NA | NA | Yes | NA | Yes |
| Target | Yes | Yes | Yes | Yes | Yes, permission-gated | Link users / haltpoints | NA | NA | NA | NA | Yes | NA | Yes |
| Haltpoint | Yes | Yes | Yes | Yes | Yes, permission-gated | Link targets | NA | NA | NA | NA | Yes | NA | Yes |
| Route | Yes | Yes | Yes, with versioning rules | Yes | Permission-gated | Assign resources where route type allows | Deep-link to Scheduler only | NA | NA | NA | Yes | NA | Yes |
| Trip | Yes | Yes | Limited by status | NA | NA | Vehicle / driver / workforce | Via Scheduler integration only | Yes | Yes | Yes | Yes | Yes | Yes |
| Adhoc Request | Yes | Yes | Limited | NA | NA | Assign to trip | NA | NA | NA | NA | Yes | Yes | Yes |

The matrix defines actions only. Final role-to-action mapping should be handled by RBAC configuration.

---
