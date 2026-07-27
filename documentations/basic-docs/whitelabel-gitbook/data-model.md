## 21. Data Model

### 21.1 BrandingConfig

| Field | Description |
| --- | --- |
| `id` | Unique branding configuration ID. |
| `organisation_id` | Organisation mapped to branding. |
| `brand_name` | Display brand name. |
| `status` | Draft, Published, Inactive, Archived. |
| `created_by` | User who created the configuration. |
| `updated_by` | User who last changed it. |
| `published_at` | Last published timestamp. |

### 21.2 BrandAssets

| Field | Description |
| --- | --- |
| `logo_url` | Primary logo. |
| `logo_dark_url` | Dark-mode logo if supported. |
| `favicon_url` | Favicon. |
| `asset_version` | Version for cache-busting. |

### 21.3 CompanyInfo

| Field | Description |
| --- | --- |
| `about_url` | About page link. |
| `phone_number` | Support/contact number. |
| `email` | Support/contact email. |
| `faq_url` | FAQ page link. |
| `privacy_policy_url` | Privacy policy link. |
| `terms_url` | Terms link. |

### 21.4 ThemeConfig

| Field | Description |
| --- | --- |
| `primary_color` | Main brand colour. |
| `disabled_web_color` | Disabled state colour for web. |
| `disabled_mobile_color` | Disabled state colour for mobile. |
| `icon_background_color` | Icon background token. |
| `duotone_icon_color` | Duotone icon token. |
| `border_radius` | Optional future token. |
| `font_family` | Optional future token. |
| `mobile_theme_supported` | Whether this configuration can be consumed by the mobile app at runtime. |
| `mobile_theme_version` | Version used by mobile app to detect new published theme config. |
| `mobile_theme_updated_at` | Timestamp of the latest mobile-consumable theme update. |

### 21.5 DomainConfig

| Field | Description |
| --- | --- |
| `domain` | Custom domain. |
| `verification_status` | DNS Pending, Verified, Failed. |
| `ssl_status` | Not Started, Provisioning, Active, Failed. |
| `created_on` | Domain added date. |
| `active` | Whether the domain is live. |

### 21.6 MobileBuildConfig

| Field | Description |
| --- | --- |
| `platform` | Android or iOS. |
| `package_name` | App package/bundle identifier. |
| `build_status` | Build workflow status. |
| `estimated_delivery_date` | Shown to customer if available. |
| `apk_url` | APK/pre-release artifact where applicable. |
| `store_url` | Live Play Store/App Store URL. |
| `approval_status` | Pending, Approved, Rejected. |
| `approval_comment` | Required when rejected. |

### 21.7 MobileRuntimeThemeState

| Field | Description |
| --- | --- |
| `organisation_id` | Organisation/company context used by mobile app. |
| `theme_version` | Published mobile theme version currently available. |
| `last_synced_at` | Last successful mobile theme sync timestamp. |
| `sync_status` | Synced, Pending, Failed, Fallback Applied. |
| `fallback_reason` | Reason mobile app used cached/default theme. |
| `supported_tokens` | List of tokens supported by the current mobile app version. |

---
