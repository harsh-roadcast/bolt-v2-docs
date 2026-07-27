---
description: >-
  Real-time fleet intelligence and configurable workflows that keep product
  owners and consumers moving in sync.
---

# Bolt V2 Fleet Management: End-User

* **What it is**: Bolt is a unified operations intelligence platform for organizations that manage fleets, field assets, and on-ground personnel. It merges real-time visibility, configurable workflows, and deep reporting into a single web experience.
* **Who it’s for**:
  * Product Owners: orchestrate programs, configure roles, and align KPIs.
  * Portal Operators: run daily operations—devices, trips, notifications, incidents, yard logistics.
  * Public Consumers: securely access shared trackers or dock data with read-only insight.
* **Why it matters**: Reduce operational blind spots, standardize compliance, and respond faster to exceptions through location-aware dashboards, AI-assisted insights, and granular alerting.

### System Philosophy: Organization-First Architecture

Bolt V2 has fundamentally shifted from a user-centric model to an **Organization-Centric architecture**.

* **Asset Ownership:** In this system, assets (vehicles, geofences, devices) are owned by an **Organization**, not an individual user. If a user leaves a company, the assets remain tied to the organization node.
* **The Hierarchical Tree:**
  * **Super Parent (Roadcast):** The root node with "God Mode" access. Roadcast manages global plans, hardware masters, and platform-wide configurations.
  * **Parent Organization:** The primary client entity (e.g., a logistics company).
  * **Child Branches:** Sub-entities or regional offices that inherit settings from the Parent but can maintain operational isolation.

#### The Organization Tree

The structure of Bolt V2 is built as a recursive tree, ensuring that permissions and billing can be managed at scale.

**Structure Hierarchy:**

1. **Level 0: Roadcast (The Root)**
   * _**Access**:_ Platform Administration.
   * _**Responsibility**:_ Creating standard plans, onboarding enterprise clients, and managing hardware masters (IMEIs, SIMs).
2. **Level 1: Enterprise Parent (Client Level)**
   * _**Access**:_ Organization Admin.
   * _**Responsibility**:_ Managing the master wallet, creating internal user roles, and configuring global geofences.
3. **Level 2: Child Branches / Regional Hubs**
   * _**Access**:_ Branch Manager / Operations.
   * _**Responsibility**:_ Day-to-day dispatch, yard management, and driver assignments.

<figure><img src=".gitbook/assets/image (12) (1).png" alt=""><figcaption></figcaption></figure>

**Inheritance Logic:**

* **Permissions:** Roles created at the Parent level are automatically available to all Child branches.
* **Data Visibility:** Parents can view all data from their Children; however, a Child branch is isolated and cannot see sibling or parent data.
* **Billing:** If an organization is created without a designated parent, it is automatically nested directly under the **Roadcast** root.

### Learn more about Bolt V2

\#insert video&#x20;

