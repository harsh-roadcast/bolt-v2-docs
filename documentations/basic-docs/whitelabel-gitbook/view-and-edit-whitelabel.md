## 18. View and Edit Whitelabel

### 18.1 View Mode

View mode should show the saved/published configuration in read-only format.

Approved read-only sections:

- Brand Setup.
- Authentication.
- Themes.
- Advanced Controls.
- Child Users.
- License Number.
- Organisation.
- Brand identity.
- App links.

![View Whitelabel — Brand Setup](../../.gitbook/assets/view_brand_setup.png)

*Brand Setup presents saved identity, contact, legal, and app-distribution values in read-only form.*

![View Whitelabel — Login and Experience](../../.gitbook/assets/view_login_experience.png)

*Login and Experience shows enabled authentication methods and the selected default.*

![View Whitelabel — Themes](../../.gitbook/assets/view_themes.png)

*Themes exposes saved colour roles, token values, and preview information without allowing accidental edits.*

![View Whitelabel — Advanced Controls](../../.gitbook/assets/view_advanced_controls.png)

*Advanced Controls shows domain and system-owner records while masking sensitive values.*

### 18.2 Edit Mode

Edit mode allows authorised users to change:

- Brand Setup.
- Login & Experience.
- Themes.
- Advanced Controls.

![Edit Whitelabel — Brand Setup](../../.gitbook/assets/edit_brand_setup.png)

*Brand Setup editing reuses the approved field groups and inline validation from creation.*

![Edit Whitelabel — Login and Experience](../../.gitbook/assets/edit_login_experience.png)

*Authentication editing preserves at least one enabled method and one valid default.*

![Edit Whitelabel — Themes](../../.gitbook/assets/edit_themes.png)

*Theme editing exposes generated roles and previews before changes are saved or published.*

![Edit Whitelabel — Advanced Controls](../../.gitbook/assets/edit_advanced_controls.png)

*Advanced Controls editing limits domain and system-owner changes to users with explicit permission.*

### 18.3 Edit Rules

- Editing a published configuration creates a draft version unless the system is explicitly immediate-save.
- User must save changes before leaving a step.
- Publishing should create a versioned record.
- Critical fields such as domain and app links may require additional validation or internal approval.

---
