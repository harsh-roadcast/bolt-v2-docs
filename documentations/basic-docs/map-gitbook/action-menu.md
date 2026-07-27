## 16. Action Menu

The selected entity action menu should expose only supported and permitted actions.

Actions supported by the current product flows include:

- Share.
- Show Trail.
- Path Replay.
- Nearby Vehicles.
- Driver.
- Immobilize.
- Parking Mode.
- Troubleshoot.
- Video Streaming where applicable.
- Sensor view where applicable.

Rules:

- Actions must be hidden or disabled when unsupported by device capability, license or permissions.
- Critical actions must use confirmation modals.
- Actions that issue commands must write to command log.
- Opening an action should preserve current selected entity context.

---
