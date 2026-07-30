## Workforce App / Mobile Trip Execution

The Bolt Workforce mobile app is the driver/field-agent execution surface for TripHub. It should expose only the trips and actions relevant to the logged-in workforce user, while syncing operational status back to TripHub web.

### Mobile navigation and trip visibility

The mobile app should include Trips as a primary navigation item. The Trips page should show:

![Mobile trip list](../.gitbook/assets/mobile-trip-list.png)

*Drivers can switch between Ongoing, Upcoming, and History while retaining trip status and progress context.*

![Mobile menu](../.gitbook/assets/mobile-menu.png)

*The Workforce menu exposes identity, attendance, roster, form, and settings actions permitted for the driver.*

- **Ongoing** trips.
- **Upcoming** trips.
- **History** trips.

Trip cards should show:

- Trip ID.
- Route name.
- Trip status such as Scheduled, In Progress, On Hold or Completed.
- Start and end location where available.
- Progress such as `3/7` or `0/7`.
- Scheduled date/time.
- Estimated or actual route distance.
- Contextual actions such as Start Trip, Cancel Trip, Put On Hold or Complete Trip based on status and permission.

Rules:

- A driver should only see trips assigned to them or to their active workforce role.
- Upcoming Scheduled trips can show Start Trip and Cancel Trip where allowed.
- Ongoing/In Progress trips should show route timeline and execution actions.
- Completed trips should be read-only and shown under History.
- On Hold trips should show paused state and should not allow target execution unless resumed by configured rules.

### Start Trip and pre-trip checklist

Start Trip should open a pre-trip safety checklist where configured. The current mobile design shows:

![Start trip and checklist](../.gitbook/assets/mobile-start-trip-checklist.png)

*Starting a trip presents route context and a mandatory pre-trip checklist when configured.*

- Route name, for example `Route A - Morning Shift`.
- Safety guidance copy.
- Pre-Trip Safety Checklist header with Trip ID.
- Checklist categories such as Fuel Check.
- Checklist progress such as `0 of 15 items checked`.
- Start Trip action.
- Check All Items / Uncheck All Items in the current design.

Rules:

- If checklist is mandatory, Start Trip should remain blocked until required checklist items are completed.
- Checklist completion must be saved with user ID, trip ID, timestamp, device timestamp and sync state.
- If offline mode is supported, checklist responses should be queued and synced with conflict-safe timestamps.
- Product must resolve the conflict between the legacy rule **No Select All for checklist execution** and the current mobile design showing **Check All Items / Uncheck All Items**.

### Route timeline and target execution

Once a trip is in progress, the mobile trip detail should show a route timeline.

![Mobile trip detail](../.gitbook/assets/mobile-trip-detail.png)

*The trip detail combines route progress, target timeline, service actions, and proof requirements.*

![Mobile trip map](../.gitbook/assets/mobile-trip-map.png)

*The mobile map shows the active route and trip progress without leaving the execution context.*

Timeline items should show:

- Haltpoint or hub name, such as Sector 18 Hub.
- Planned or actual time.
- Target name and target ID.
- Service location/address.
- Pickup/drop location label where route type requires it.
- Target state.

Supported target states include:

- Pending.
- En Route.
- Picked.
- No Show.
- Missed.
- Completed, where route type uses generic service completion instead of pickup/drop language.

Rules:

- Target state updates must write back to TripHub web in near real time where connectivity exists.
- Each target update must capture actor, timestamp, location and source device.
- Route-type configuration should control which labels appear: Picked/No Show for school transport, Completed/Missed for waste or service operations, Pickup/Drop/Exchange for logistics.
- Missed or No Show states should require reason if the route type marks reason capture mandatory.

### Proof capture

Mobile execution should support proof capture when configured.

The current mobile design includes a mandatory Photo field with Capture Photo and Clear actions.

Rules:

- Proof requirements should be configurable per route type, trip, target type or service type.
- Supported proof types include photo, signature, file upload and form response.
- Mandatory proof should block target completion until captured.
- Captured proof must be linked to trip ID, route ID, target/haltpoint ID, actor, timestamp, coordinates and upload/sync state.
- User should be able to clear and retake proof before submission where allowed.

### Completing a trip

Mobile should allow Complete Trip only when the user has execution permission and trip state allows completion.

Rules:

- If all required targets are completed, Complete Trip should show final confirmation.
- If incomplete targets remain, show a warning. The current mobile design shows copy similar to `You have 4 targets remaining!` with a confirm action `Yes, Complete Trip`.
- Completing with remaining targets should mark unresolved targets as missed, skipped or pending-close based on configured route-type rules.
- Completion must capture actual end time, driver location, remaining-target summary and final proof/checklist status.

### Put On Hold from mobile

The current mobile design exposes Put On Hold from trip execution.

Rules:

- Put On Hold should require a reason if configured.
- Trip status should change to On Hold / Paused.
- Admin/supervisor should see the hold event on web.
- Target execution should be disabled while trip is on hold unless resume rules allow the driver to continue.

### Mobile adhoc request

The mobile app should support driver-created adhoc requests where the route type allows it.

![Mobile adhoc request](../.gitbook/assets/mobile-adhoc-request.png)

*The driver captures site evidence and location details before submitting an additional service request.*

The current mobile design includes:

- Target Name.
- Latitude.
- Longitude.
- Address.
- Type.
- Submit Ad-Hoc Request action.
- Use Existing Target / Create New Target option.
- Validation state for required fields.

Rules:

- Adhoc request creation should be available only for route types where `Allow Adhoc Requests` is enabled.
- Driver-created adhoc requests should not mutate the master route by default.
- If `Save Adhoc Targets` is enabled, the system should create or queue a permanent target after approval or configured auto-save behavior.
- Submitted adhoc request should appear in web pending queue, assigned trip, or current trip timeline based on configuration.

### Mobile SOS, breakdown and call admin

The mobile app should support safety and exception actions from the driver surface.

![Mobile SOS action](../.gitbook/assets/mobile-sos.png)

*SOS remains available from the active driver surface and sends the current trip and location context.*

![Mobile call-admin state](../.gitbook/assets/mobile-call-admin.png)

*Call Admin communicates connection state clearly and provides an explicit End Call action.*

Supported actions:

- SOS.
- Report Vehicle Breakdown.
- Confirm Breakdown.
- Call Admin.
- End Call.

Rules:

- SOS should create a high-priority safety event with driver, trip, vehicle, location and timestamp.
- Report Vehicle Breakdown should show confirmation before changing trip state.
- Confirmed breakdown should update trip status to Breakdown and notify admin/supervisor.
- Call Admin should show connected and ended states. The design includes states such as `Connected with Admin`, `You can now speak with the admin`, `End Call`, `Call Ended` and `Your conversation with the admin has ended`.

### Driver onboarding and identity

The mobile design includes a driver identity onboarding flow.

Supported onboarding steps:

- Face verification.
- Driver license entry.
- Welcome/setup screen.

Rules:

- Identity verification should be configurable by organisation or route type.
- If identity verification is mandatory, Start Trip should be blocked until verification is complete.
- Driver license data should be validated and stored according to the organisation's compliance policy.

### Mobile forms

The mobile Forms surface should support route/trip-linked forms and compliance workflows.

![Mobile form centre](../.gitbook/assets/mobile-form-center.png)

*Form Centre provides a single mobile entry point for trip-linked, safety, survey, and compliance forms.*

Rules:

- Forms should be available from Menu and/or Trip context depending on form type.
- Trip-linked forms should attach responses to the active trip and relevant target/haltpoint where applicable.
- Form responses must support offline queueing if offline execution is in scope.


### Mobile OTP, POD and cancellation requirements

Target/service execution must support OTP and proof-of-delivery patterns where configured by route type.

OTP rules:

- OTP verification may be required for pickup/drop/service completion.
- Wrong OTP must show an error and allow retry within configured attempt limits.
- Exceeded retry attempts should require admin override, alternate proof or target exception reason based on route type.
- OTP verification event must store target/service-request ID, trip ID, attempt count, timestamp and actor.

POD rules:

- POD may require mandatory photo, optional signature and additional notes.
- Photo proof must validate camera permission, file size, upload state and offline queueing if offline is supported.
- Signature, notes and proof requirements must be controlled by Route Type completion configuration.
- Completion must be blocked until mandatory POD fields are submitted.

Cancel Trip rules:

- Cancel Trip must require reason selection, optional details and confirmation.
- Cancellation rate, driver rating, or account-suspension messages must only appear when the connected scoring and penalty rules are configured. Otherwise, the claims must be removed from the user-facing copy.
- Cancellation must notify admin/supervisor and update trip status based on cancellation policy.

### Mobile adhoc request detail

Adhoc request creation on mobile should start with site-photo capture where shown in the design.

Rules:

- Driver should capture or upload site photo before submitting an adhoc request if route type requires proof.
- System should run nearby-target matching based on current location and selected service area.
- If a nearby eligible target exists, the user should choose Use Existing Target.
- If no matching target exists or the user has permission, the user may choose Create New Target.
- Created adhoc targets must follow Route Type retention rules: retain in master target table, queue for admin approval, or keep as trip-instance-only request.
- Adhoc submit must handle loading, duplicate match warning, permission denied, offline queue and upload failure states.

### Mobile general states

The mobile app must cover operational states beyond the happy path:

- Loading trip assignments.
- No active shift/schedule empty state.
- No ongoing trips.
- No upcoming trips.
- Offline mode / queued actions.
- Permission denied for camera, location, microphone or phone.
- Sync failed with retry.
- Stale assignment: trip was changed, reassigned, cancelled or completed on web while driver is viewing it.
- Partial sync: checklist/proof uploaded but status update failed.
- App resume after being killed during active trip.
