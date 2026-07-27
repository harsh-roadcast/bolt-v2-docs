## 2. How to Use This Guide

This guide is structured so product, design, engineering, QA, support and operations teams can use the same source:

- **Sections 3–8:** product problem, goals, scope, users, permissions and information architecture.
- **Sections 9–19:** Command Center, stream actions, Device History, PAP Incidents and investigation workflows.
- **Sections 20–24:** data entities, state models, backend behavior, performance and security.
- **Sections 25–30:** analytics, acceptance criteria, open decisions, implementation notes, release phases and summary.

Screenshots are embedded beside the workflow they explain. Every image uses a relative `assets/...` path so the Markdown can be imported with this package without any external design links.

### 2.1 Requirement Traceability

Requirements in this document are interpreted using the following order:

1. **Confirmed product decisions** explicitly stated in this PRD.
2. **The embedded product screens** for layout, labels, actions and navigation.
3. **Functional rules in this document** for backend behavior, permissions, evidence integrity and system states.
4. **Open decisions** where the design or current scope does not define a final rule.

If the implementation cannot support a designed interaction because of device capability, network limits, storage limits or permissions, the interface must show a specific unavailable state instead of silently hiding the failure.

---
