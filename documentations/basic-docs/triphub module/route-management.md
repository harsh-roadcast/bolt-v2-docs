## Route Management

Routes define the planned operational sequence or service area used to create trips. Routes should support both sequence-based and service-area-based operating models.

### Route list

Route list should support:

- Empty state when no routes exist.
- Create Route CTA.
- Download Report.
- Filters and applied filter state.
- Table view with row actions.
- Map view where available.
- Route detail/edit entry from row action.
- Schedule state showing whether a route is scheduled or not.

Standard columns:

- ID
- Name
- Haltpoints
- Distance
- Start Point
- End Point
- Created On
- Time to Complete
- Shifts
- Last Updated On
- Actions

Latest Trip Changes design also shows route-related status, progress and trip columns in updated route/trip contexts; engineering should confirm final table model per page.

![Routes list](../.gitbook/assets/route-list.png)

*The current Routes list combines route metadata, haltpoint counts, scheduling context, filters, and operational actions.*

### Route empty state

The empty state should guide the user to create routes after targets/haltpoints/service areas are ready. It should not over-explain setup if upstream entities already exist.

![Route setup onboarding](../.gitbook/assets/route-empty-onboarding.png)

*The first-time state explains which upstream entities must be configured before route creation.*

![Route-ready empty state](../.gitbook/assets/route-empty-ready.png)

*Once prerequisite data is available, the empty state shifts to a direct route-creation action.*

### Route editing rules

Business rules from TripHub Solution Documentation:

- Reordering haltpoints is allowed while editing a route, subject to route status, permissions and dependency checks.
- Adding a new target to an existing route is not allowed by default. If the target set changes materially, the user must create a new route or use an approved route-versioning workflow.
- Existing route edits must not corrupt already-created trips. If an active or historical trip exists, route changes should either create a new route version or apply only to future trips.
- Service type changes are allowed only where the target/service request has not already reached an immutable execution state.

### Route Status Model

Routes exist only after they are created. V1 does not require a Draft/In Setup route state.

| Route Status | Meaning | TripHub behavior | Editing behavior |
|---|---|---|---|
| Active | Route has been created and is available for manual trip creation or operational use. | Can be selected for trip creation where permissions and route type allow. | Operational edits may create a new route version. |
| Scheduled | Route has been linked to Scheduler / Shift Master and may generate trips through Scheduler. | Shows shift/schedule summary and generated trips where applicable. | Add Haltpoints and other operational edits are allowed until a linked trip is started; Scheduler impact validation is required. |
| Disabled | Route is blocked for future manual trip creation and future scheduling. | Existing ongoing/completed trips remain visible for history and audit. | Editing is blocked except permitted administrative metadata or re-enable workflows. |

Route statuses are separate from Trip statuses. Route status controls route availability and editability; Trip status controls execution state of a generated or manually created trip.

### Route empty-state matrix

The Route page must show different empty/setup states based on upstream readiness. The generic empty state is not sufficient.

| State | Eligibility condition | Primary copy intent | Primary CTA |
|---|---|---|---|
| No Bins/Targets and no Haltpoints | No eligible targets and no eligible haltpoints exist for selected organisation/route type. | User must first create service points before route planning. | Create Target / Create Bin |
| Bins/Targets created, no Haltpoints | Eligible targets exist but no haltpoints exist. | User must group targets into haltpoints or create haltpoint during target/bin creation. | Create Haltpoint |
| Haltpoints created, no Bins/Targets | Haltpoints exist but no linked eligible targets exist. | User must create/link targets before route execution can be meaningful. | Create Target / Link Target |
| Bins/Targets and Haltpoints both created | Both upstream entities exist but no route exists. The exact difference between this state and Everything Ready remains an open decision. | User has the required upstream entities but may still need route-type/configuration/permission readiness. | Create Route or setup CTA based on final decision |
| Everything ready | Product decision pending. This may either merge with the previous state or represent the condition where target data, haltpoints, route type configuration and user permission are all valid. | Encourage first route creation without additional setup explanation. | Create Manual Route / Create Auto Route |

Rules:

- While creating a Bin or Target, the user should be able to create a Haltpoint at the same location when this capability is enabled for the organisation.
- Empty-state CTAs must respect permissions, organisation scope and route type.
- If an upstream entity exists but is disabled or outside the selected organisation/territory, it must not count toward readiness.
- The overlap between **Bins/Targets and Haltpoints both created** and **Everything ready** remains an open decision and should not be treated as a final implementation rule until product/design confirms the distinction or merges the states.

### Scheduler integration: route-level touchpoints

Scheduler and Shift Master are handled as a separate module. TripHub defines only the integration points required to show route schedule state, navigate users to Scheduler actions, and consume trips generated by Scheduler.

TripHub-owned requirements:

- The Route List must include a **Shifts** column when Scheduler integration is enabled.
- A route may show one shift, multiple shifts or no shifts.
- If no shift is attached, show `--` and treat the route as unscheduled.
- Clicking a shift should open a schedule information panel or deep-link into the Scheduler module, depending on the final Scheduler navigation pattern.
- Scheduled route banners must show the shift name or schedule summary and an **Edit Schedule** action.
- Unscheduled route banners must show **Schedule Route** where the user has permission.
- **Create Shift & Schedule** must open the Scheduler / Shift Master flow in a new tab or new module context.
- Recurrence-based trip generation is owned by Scheduler. TripHub receives generated trip instances and shows them in the Trip List as scheduled/upcoming trips.
- When a route is edited, disabled or versioned, TripHub must request schedule-impact validation from Scheduler before saving changes that affect scheduled routes or already-generated future trips.
- Already-generated future trips should update based on the route update until the trip is started.
- Ongoing/started trips must remain unchanged if the linked route or schedule is edited.

Scheduler-owned requirements:

- Shift creation and shift policy.
- Schedule timezone, start/end date, recurrence, exceptions and holiday rules.
- Missed-generation handling and retry policy.
- Editing scope for current occurrence, future occurrences or all occurrences.
- Scheduler UI and recurrence policy details when a route is edited, disabled or versioned. TripHub only consumes Scheduler impact validation and generated-trip updates.

![Live scheduler dashboard](../.gitbook/assets/live-scheduler-dashboard.png)

*The live Scheduler view is retained here only to explain the TripHub-to-Scheduler handoff and generated-trip relationship.*

### Route editing, Add Haltpoints and disable behavior

The product must distinguish between adding or removing haltpoints and adding new targets inside an existing haltpoint.

Rules:

- Route editing exposes **Add Halt Points**. In V1, adding haltpoints is allowed for Active routes and for Scheduled routes until a linked trip is started.
- Once a trip is started from a route, that started trip must retain its execution snapshot and must not be mutated by later route edits.
- Adding a haltpoint to a route must update already-generated future trips until those trips are started.
- Adding a target inside an existing haltpoint should not automatically affect an existing route unless the route is explicitly refreshed or updated through the route-edit flow.
- Scheduled routes require Scheduler-impact validation before route edits are saved because already-generated future trips may need to update.
- Disabling a route must block new manual trip creation from TripHub and future scheduling. Ongoing/started trips remain unchanged.
- Active trips continue unchanged unless an admin separately puts them on hold, marks breakdown, completes/ends them or reassigns work.
- Disable confirmation must show dependency checks returned by TripHub and Scheduler, including active trips, upcoming generated trips, linked schedules and linked territories.
- Route name and description changes do not create a new route version.
