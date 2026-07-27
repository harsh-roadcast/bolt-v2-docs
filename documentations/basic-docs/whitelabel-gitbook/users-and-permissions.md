## 6. Users and Permissions

| User Type | Description | Expected Access |
| --- | --- | --- |
| Organisation Owner | Customer-side business owner with billing and configuration authority. | Purchase module, configure branding, publish changes. |
| Organisation Admin | Customer-side admin responsible for operational setup. | Configure branding if RBAC allows. |
| Reseller / MSP Admin | Partner managing branding for child organisations. | Configure or assist branding for assigned organisations. |
| Support Admin | Internal support user assisting customers. | View/edit based on internal permissions; may impersonate or configure on behalf of customer if authorised. |
| Super Admin | Internal platform admin. | Full access, override and recovery controls. |
| Viewer | Read-only admin or stakeholder. | View branding configuration and app status only. |

### 6.1 RBAC Permissions

Suggested permissions:

| Permission | Description |
| --- | --- |
| `branding.view` | View branding configuration and current published state. |
| `branding.create` | Create a new whitelabel configuration. |
| `branding.edit` | Edit draft branding configuration. |
| `branding.publish` | Publish branding changes. |
| `branding.delete` | Delete or deactivate a whitelabel record, subject to safety rules. |
| `branding.domain.manage` | Add, verify and remove custom domains. |
| `branding.auth.manage` | Configure login and authentication experience. |
| `branding.theme.manage` | Configure theme tokens and colour roles. |
| `branding.mobile_app.track` | View mobile app build status and delivery details. |
| `branding.mobile_app.approve` | Approve or reject a mobile app build preview. |
| `branding.rollback` | Restore previous published configuration. |

---
