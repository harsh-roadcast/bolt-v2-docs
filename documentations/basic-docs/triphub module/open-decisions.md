## Open Decisions

- Whether `Draft` is required as a new save-as-draft status. It is not part of the confirmed current status model.
- Whether `Approved` is a Route status, Trip status or approval state.
- Final list of Route Types for first release.
- Which advanced Route Type configuration controls ship in the first release versus later vertical-extension phases. Foundational Route Type configuration is required earlier for route creation and mobile execution.
- Final target labels per vertical: Bin, Student, Customer, Asset, Target.
- Whether target creation from driver adhoc flow should save as permanent target by default or only by admin approval.
- Service area mismatch behavior: warning or hard block.
- Re-run behavior: full original route vs missed targets only.
- Offline Workforce App requirements and sync conflict handling.
- Attendance blocking rules for absent/not-marked workforce.
- Checklist mandatory rules by route type.
- Parent app scope for Bus993 first release.
- API/database sync requirements for target import.
- KML validation rules and supported geometry types.
- Whether route optimisation is internal logic or exposed as a user-selectable mode.
- Whether mobile pre-trip checklist should keep Check All / Uncheck All or follow the legacy no-select-all compliance rule.
- Whether mobile identity verification is mandatory for all drivers or route-type/organisation configurable.
- Whether drivers can self-resume an On Hold trip or only admins/supervisors can resume it.
- Whether Complete Trip with incomplete targets should mark remaining targets as Missed, Skipped or Pending Review.
- Whether mobile adhoc requests outside the assigned service area should be blocked, warned or allowed with supervisor approval.
- Exact offline-sync rules for mobile proof, checklist, target state, SOS and breakdown events.
- Whether Call Admin uses in-app calling, PSTN call, VoIP or a future support integration.

- Whether Target Setup supports only organisation-level assignment or inheritance through organisation hierarchy.
- Whether target attribute schemas require draft/published/versioned states before being used in production forms.
- Whether field type changes are blocked after data exists or handled through migration rules.
- Whether Route Type configuration ships with the complete control set or a reduced first-release subset.
- Whether Vehicle Assignment Allowed should affect route creation, trip creation or both.
- Whether Route Type service types are limited to Pickup, Drop and Exchange in the first release.


### Additional open decisions

- Should the route empty states **Bins/Targets and Haltpoints both created** and **Everything ready** remain separate, or be merged into one route-ready empty state?
- Does `Unlinked` haltpoint mean not linked to any route, or not linked to any active route?
- Are overlapping territory boundaries allowed, warned or blocked?
- Do child territories inherit routes, users or geofences from parent territories?
- Which additional route-edit fields, if any, should create a new route version beyond the confirmed operational triggers?
- What exact contract should Scheduler expose when TripHub edits, disables or versions a scheduled route?
- Do duplicated trips retain driver, vehicle, date, adhoc work and proof configuration by default?
- Should cancellation-rate, driver-rating, and account-suspension copy be removed from TripHub mobile screens until a connected scoring policy exists?
- Are mandatory and flexible break policies configured at route type, Scheduler shift, organisation or driver level?
- What TripHub-facing offline behavior is required for OTP, POD, adhoc, and breakdown events while deeper sync-engine rules remain with the connected mobile/offline-sync specification?
- Which Forms Centre surfaces are TripHub-scoped versus owned by the connected Forms/Checklist specification?

---
