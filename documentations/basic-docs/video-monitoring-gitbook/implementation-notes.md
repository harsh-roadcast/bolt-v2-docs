## 28. Implementation Notes

- Treat Command Center and PAP Incidents as separate pages with shared device, channel and incident services.
- Keep live stream sessions separate from evidence clip playback.
- Use device capability checks before rendering stream actions.
- Preserve user layout/filter preferences where useful, but avoid persisting temporary incident filters permanently.
- Maintain stream card position during reconnect attempts to avoid disorienting operators.
- Build incident cards and incident detail from the same source metadata to avoid mismatched evidence.
- Use server-side aggregation for heat-map and hotspot views at scale.
- Add clear telemetry for stream failures so support teams can identify device, network and backend issues.

---
