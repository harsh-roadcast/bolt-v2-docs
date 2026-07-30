## Attendance Integration

TripHub should integrate with HRMS and FaceSync attendance where configured.

Attendance sources:

- Facial Recognition.
- Manual Attendance.
- HRMS Attendance APIs.

For each assigned workforce member, TripHub should show:

- Present.
- Absent.
- Not Marked.

Filters:

- Present.
- Absent.
- Attendance Pending.

Rules:

- Attendance should be fetched before trip start validation where mandatory.
- If driver attendance is mandatory and absent/not marked, Start Trip should be blocked or warning-based depending on route type.
- Attendance sync failures should not silently mark employees absent.
- Attendance status and sync timestamp must be visible in trip detail when attendance rules apply.


### FaceSync mobile states

FaceSync check-in/check-out must cover operational states where TripHub depends on identity or attendance verification:

- Verification in progress.
- Verification failed with retry.
- Camera permission denied.
- Multiple active session detected.
- Check-in already active.
- Check-out without active check-in.
- Offline verification unavailable or queued, based on technical feasibility.
- Identity mismatch requiring admin override.

If FaceSync is required by Route Type, Start Trip, Resume Trip or target completion must block until the relevant verification is complete.

---
