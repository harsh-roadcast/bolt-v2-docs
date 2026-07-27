## 23. Empty, Error and Edge States

| State | Expected Behaviour |
| --- | --- |
| No whitelabel configured | Show empty state with CTA to create or unlock branding. |
| Branding not purchased | Show locked preview and purchase CTA. |
| Upload failed | Show file-level error and retry option. |
| Invalid URL | Show inline error and block save if field is mandatory. |
| Domain already used | Show conflict error and prevent verification. |
| DNS not verified | Keep domain inactive and show setup instructions. |
| SSL failed | Keep domain inactive and show retry/support guidance. |
| Unsaved changes on cancel | Show confirmation dialog. |
| Entitlement expired | Apply fallback or preserve existing branding based on product decision. |
| Mobile build rejected | Require comment and notify support/internal owner. |
| Theme contrast failure | Warn or block publish depending on severity. |
| Mobile theme sync failed | Mobile app falls back to cached last-known-good or default Bolt theme and logs failure. |
| Mobile app version does not support token | Ignore unsupported token and use default for that role. |

---
