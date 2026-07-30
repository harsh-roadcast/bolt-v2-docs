## SOS and Emergency Management

SOS is included in TripHub V1 as a driver-triggered emergency event during active trip execution.

TripHub-owned SOS scope:

- Show SOS action during active TripHub trip execution where route type/organisation configuration allows it.
- Create SOS event with trip, route, vehicle, driver/user, location and timestamp context.
- Show SOS sent acknowledgement on mobile.
- Show SOS event in TripHub trip detail, timeline and audit trail.
- Preserve SOS history for operational review and reporting events.

Connected Alerts/SOS platform scope:

- Escalation workflow.
- Notification routing.
- Recipient configuration.
- SMS/email/push/call delivery policies.
- Escalation SLA and retry policy.

TripHub must pass the correct event context to the Alerts/SOS platform without duplicating the full alert-escalation rules.


### SOS acknowledgement and call states

Mobile SOS must include acknowledgement and escalation states:

- SOS sent acknowledgement with timestamp and location.
- SOS failed/retry state if network submission fails.
- Admin-notified or escalation-in-progress state where supported.
- Outgoing internet call to admin.
- Incoming admin call.
- Answer call.
- Connected duration.
- Call ended.
- Call failed and retry.

All SOS/call events must be associated with trip, driver, vehicle, route and location where available.

---
