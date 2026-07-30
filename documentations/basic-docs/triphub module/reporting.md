## Reporting

TripHub owns the reportable events, source data, and operational states that Reports can consume. The connected Reports specification owns implementation details such as report columns, filters, grouping, export formats, scheduling, permissions, and configured-label handling.

TripHub should support operational and compliance report outputs for:

- Trip Performance.
- Route Performance.
- Target Completion.
- Missed Targets.
- Haltpoint Coverage.
- Attendance Compliance.
- Break Analysis.
- Checklist Compliance.
- Route Deviations.
- Adhoc Requests.
- Breakdown Events.
- SOS Events.
- Student Pickup/Drop Reports.

Reporting rules:

- Reports should preserve route/trip version at time of execution.
- Adhoc work should be reportable separately from planned route targets.
- Missed target reason must be reportable where captured.
- Exports should respect organisation hierarchy and RBAC.

---
