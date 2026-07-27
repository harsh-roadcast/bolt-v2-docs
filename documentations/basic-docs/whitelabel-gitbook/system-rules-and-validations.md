## 22. System Rules and Validations

### 22.1 Asset Validation

- Logo upload accepts PNG, JPG and JPEG based on approved interface copy.
- Max file size shown in the approved interface is 20 MB.
- Recommended favicon dimension shown in the approved interface is 512 × 512 px.
- Unsupported files must show inline error.
- Asset replacement must not delete old asset until new asset is saved.

### 22.2 URL Validation

- About, FAQ, Privacy Policy and Terms URLs must use HTTPS.
- Android and iOS app URLs must be valid store/app links where applicable.
- Domain must not include protocol when being added as a domain record.

### 22.3 Theme Validation

- Primary colour must be a valid hex value.
- Generated colour roles should meet contrast requirements where they are used for text/action states.
- Invalid colour states should block publish if they create critical accessibility failure.
- Mobile-specific theme tokens must be validated separately from web tokens.
- Unsupported mobile tokens should be ignored safely rather than breaking the mobile UI.

### 22.4 Authentication Validation

- At least one authentication method must remain enabled.
- Default method must be one of the enabled methods.
- OTP login must not be enabled unless OTP infrastructure is available.

### 22.5 Entitlement Validation

- User cannot create or publish branding unless the Branding add-on is active.
- User cannot access mobile build tracking unless app branding is included in entitlement.
- Expired entitlement behaviour is an open decision.

---
