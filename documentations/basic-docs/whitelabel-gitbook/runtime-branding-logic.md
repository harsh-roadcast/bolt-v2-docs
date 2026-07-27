## 20. Runtime Branding Logic

At runtime, Bolt should resolve branding using the active organisation context.

### 20.1 Resolution Order

Recommended resolution order:

```text
Custom Domain / Hostname
→ Organisation Branding Config
→ Parent/Reseller Branding Config, if inheritance is enabled
→ Default Bolt Branding
```

### 20.2 Fallback Rules

- If logo fails to load, use default Bolt logo.
- If favicon is missing, use default favicon.
- If colour token is missing, use default Bolt token.
- If domain verification fails, do not route traffic to that domain.
- If email sender is unverified, use default sender.

### 20.3 Cache and Propagation

- Web branding updates should clear or refresh CDN/app-shell cache.
- Users should see updated branding after refresh or within a defined propagation window.
- Propagation window must be confirmed by engineering.

### 20.4 Mobile Runtime Branding Resolution

Mobile runtime branding should resolve from the active organisation/company context after authentication. The mobile app should request the latest published Branding configuration, apply only supported mobile tokens and retain a cached last-known-good configuration when the network is unavailable.

Recommended mobile resolution order:

```text
Logged-in User Organisation / Company ID
→ Published Branding Config
→ Supported Mobile Theme Tokens
→ Cached Last-known-good Mobile Branding Config
→ Default Bolt Mobile Theme
```

The app must not apply a partial theme if required tokens are missing or invalid. In that case, it should fall back to default Bolt mobile theme or the last-known-good configuration and log the failure.

---
