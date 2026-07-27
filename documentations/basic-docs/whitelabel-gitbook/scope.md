## 5. Scope

### 5.1 In Scope

- Branding / Whitelabel Manager list view.
- Create Whitelabel flow.
- View Whitelabel detail flow.
- Edit Whitelabel flow.
- Brand Setup configuration.
- Authentication / Login & Experience configuration.
- Themes configuration.
- Advanced Controls configuration.
- Domain management.
- Legal and compliance links.
- App distribution links.
- White-label module entitlement and locked/unlocked state.
- Client-side self-serve setup direction.
- Admin-side operational management for support/internal teams.
- Mobile runtime theme reflection for supported theme tokens.
- Mobile app build tracking and approval model as a supported workflow.
- Audit logs and configuration history.
- Fallback to default Bolt branding when custom branding is missing or inactive.

### 5.2 Out of Scope for Initial Release

- Full drag-and-drop custom login page builder.
- Custom CSS injection.
- Full white-labelled mobile app build automation without internal developer intervention.
- App Store / Play Store identity changes without the mobile build workflow.
- Launcher icon, package name, bundle ID, store listing or bundled splash assets through runtime theme sync.
- App Store / Play Store submission automation.
- SMS template branding.
- Custom fonts unless explicitly enabled by engineering.
- Per-screen UI layout customisation.
- Arbitrary payment-gateway key management unless tied to a separate integration/configuration module.

### 5.3 Approved Interface Scope

The approved Admin Whitelabel interface confirms the following top-level Whitelabel Manager areas:

- Whitelabel list with Brand Name, Organisation, Date Created and Actions.
- Create Whitelabel with four steps: Brand Setup, Authentication, Themes and Advanced Controls.
- View Whitelabel details with tabs for Brand Setup, Authentication, Themes and Advanced Controls.
- Edit flows for Brand Setup, Login & Experience, Themes and Advanced Controls.
- Brand identity fields including Brand Name, Organisation, Brand Logo and Favicon.
- Company, legal and app access/distribution fields.
- Authentication method configuration.
- Theme colour configuration and generated UI colour roles, including mobile-specific token handling where supported.
- Domain management under Advanced Controls.

---
