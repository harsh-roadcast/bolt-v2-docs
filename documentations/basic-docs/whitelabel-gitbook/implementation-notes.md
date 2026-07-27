## 30. Implementation Notes

- Treat the approved interface labels, fields, tabs, and step order shown in this package as the implementation baseline.
- Keep example records and sample values out of production fixtures unless they are explicitly anonymised test data.
- Use the organisation context and entitlement service as the authority for configuration access.
- Resolve runtime branding from a published, versioned configuration; never apply an incomplete draft.
- Keep web runtime theming, mobile runtime theming, custom-domain activation, and branded app builds as separate delivery paths.
- Record every publish, rollback, domain change, build approval, and internal override in the audit trail.
- Preserve the default Bolt theme and assets as a last-known-safe fallback.
- The exact commercial packaging, entitlement-expiry behavior, mobile refresh cadence, and app-build SLA remain product decisions and must be confirmed before release.

---
