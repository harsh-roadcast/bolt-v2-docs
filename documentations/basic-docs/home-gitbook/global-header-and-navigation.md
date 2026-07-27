## 23. Global Header and Navigation

Home uses the standard Bolt web shell.

### 23.1 Header

The header includes:

- Active page name.
- Notification entry.
- User avatar and name.
- Current organisation or impersonation context where configured.

### 23.2 Left navigation

- Home is the active destination.
- The approved state uses collapsed navigation.
- Existing expand, collapse, tooltip, and keyboard behavior is preserved.
- Role restrictions continue to control destination visibility.

### 23.3 Greeting

The page greeting follows the pattern:

- `Hello {display name}, welcome back`
- `Monitor key updates and take quick actions right from here.`

The displayed name must use the authenticated user's permitted display value and safely escape unexpected characters.

---
