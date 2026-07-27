## 26. Acceptance Criteria

### 26.1 Entitlement and Access

- Users without active Branding entitlement see locked state and purchase CTA.
- Users with active entitlement can access Branding configuration if RBAC allows.
- Users without edit permission can only view current configuration.

### 26.2 Whitelabel List

- List displays Brand Name, Organisation, Date Created and Actions.
- Search and filters are available.
- Pagination works for more than one page of records.
- Row actions respect permissions.

### 26.3 Create Flow

- User can complete Brand Setup, Authentication, Themes and Advanced Controls steps.
- `Save & Continue` persists step data.
- Required fields are validated inline.
- Cancel with unsaved changes shows confirmation.

### 26.4 Brand Setup

- User can add brand name, organisation, logo, favicon, company information, legal links and app links.
- URLs must use HTTPS where required.
- Invalid assets or URLs are blocked with useful errors.

### 26.5 Authentication

- User can select supported authentication method.
- One default method is maintained.
- Invalid combinations are blocked.

### 26.6 Themes

- User can set primary colour.
- System generates or displays UI colour roles.
- Theme preview or token display reflects selected colour.
- Accessibility-critical contrast failures are handled.
- Supported mobile theme tokens are generated or exposed alongside web tokens.
- Published mobile-supported theme changes are available to the mobile app through runtime configuration.

### 26.7 Advanced Controls

- User can add and view domains.
- Domain status is visible.
- Unverified domains cannot go live.

### 26.8 Mobile Theme Reflection

- The Bolt mobile app reflects published branding theme values wherever runtime theming is supported.
- Primary colour, disabled mobile colour, icon background and duotone icon colour are available to mobile as configurable tokens.
- Mobile theme changes do not require a new build when the change is limited to runtime-supported tokens.
- Mobile app falls back safely to cached/default Bolt theme if sync fails.
- App-store identity changes are not treated as runtime mobile theme changes.

### 26.9 Mobile Build Tracking

- App build status can be tracked when mobile app-store branding is included.
- Estimated delivery date is visible once initiated.
- Client approval/rejection is supported.
- Rejection requires comments.
- Build history is preserved.

---
