## 19. Save, Publish, Versioning and Rollback

### 19.1 Draft vs Published

The platform should distinguish between:

| State | Description |
| --- | --- |
| Draft | Unsaved or saved-but-unpublished configuration changes. |
| Published | Active configuration used by end users. |
| Archived Version | Older published configuration available for audit/rollback. |

### 19.2 Publish Behaviour

- Publishing applies changes to the selected organisation.
- Web theme and asset changes should propagate without app redeploy where technically supported.
- Runtime-supported mobile theme-token changes should sync through mobile configuration fetch and should not require a mobile app build.
- Domain changes become active only after verification and SSL readiness.
- Mobile changes that affect app-store identity, launcher assets, package/bundle identity or bundled app assets must initiate the mobile build workflow instead of immediate live update.

### 19.3 Version History

Older builds and published versions must be stored to avoid conflicts. The same versioning principle applies to web branding.

Requirements:

- Store who changed what and when.
- Store previous published version.
- Allow rollback for web branding where safe.
- Store mobile build version and approval history.

---
