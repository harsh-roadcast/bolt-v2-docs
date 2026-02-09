---
description: >-
  This section outlines the visual standards, interaction logic, and user
  experience principles that define the Bolt V2 platform.
---

# UI/UX Specifications & Design System

#### Unified Design Language

Bolt V2 uses a utility-first design system built on **Tailwind CSS**. The goal is to provide a clean, high-performance interface that prioritizes data visibility.

* **Management Hub Approach:** The interface is split into two distinct modes:
  * **Admin Side (Roadcast):** Designed for high-density data management, bulk configurations, and global oversight.
  * **Client Side:** Designed for operational speed, featuring simplified menus focused on tracking and day-to-day logistics.
* **Consistency:** Every page follows a standard layout: a collapsible **Navigation Sidebar** on the left, a **Contextual Navbar** at the top, and a dynamic **Workspace** in the center.

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### The Contextual User Journey

The most important UX principle in Bolt V2 is **Organization Context**.

* **Workspace Awareness:** The top navbar always displays the name of the active Organization. This is a constant visual reminder that the data being viewed is limited to that specific branch or parent.
* **Slide-Out Workflows:** To prevent "context loss," the app avoids excessive page jumping. When you click on a vehicle or trip, a **Side Panel** slides out from the right. This allows users to view details or edit settings while still keeping the primary map or list visible in the background.

#### Smart Interaction Components

We use a set of custom components to handle complex data entry and display tasks simply.

* **Form Generator:** Instead of hard-coded forms, Bolt V2 uses a schema-based generator.
  * **Validation:** Forms provide instant feedback (e.g., matching passwords, valid IMEI formats).
  * **Requirement Indicators:** Fields marked with a red asterisk are mandatory for the backend logic to process.
* **Generic Table System:** All data lists (Users, Vehicles, SIMs) use a high-performance grid.
  * **Bulk Actions:** Users can select multiple rows to perform actions like "Bulk Suspension" or "Assign to Group."
  * **Skeleton Loading:** While data is being fetched from the GraphQL server, the UI displays grey "shimmer" placeholders to prevent the screen from looking empty or broken.

#### Visual Feedback & System Health

The platform uses color and motion to communicate state without requiring the user to read long messages.

* **Status Toasts:** Small notification boxes appear in the corner to confirm actions:
  * **Green:** Success (e.g., "License purchased successfully").
  * **Orange:** Warning (e.g., "Wallet balance is low").
  * **Red:** Error (e.g., "403: You do not have permission to view this section").
* **Map Marker Logic:** Vehicle icons on the map use a traffic-light color system (Green/Yellow/Red/Grey) to indicate engine and connection health instantly.

<figure><img src="../../.gitbook/assets/image (4) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Hardened Security UX (PRD Case 9.3)

Security is woven into the user experience through "Session Versioning" and strict access logic.

* **Permission-Based Visibility:** If a user’s role does not allow "Delete" access, the delete button is **completely removed** from the UI, not just greyed out. This reduces clutter and prevents unauthorized attempts.
* **Force-Logout Interaction:** If an administrator suspends a user while they are logged in:
  1. The next interaction the user makes will trigger a **Security Modal**.
  2. The modal informs the user that their session is no longer valid.
  3. The user is automatically redirected to the Login page.
* **Impersonation Indicators:** When an Admin uses the "Impersonate" feature, the UI adopts a distinct visual highlight (often matching the client’s brand colors) to signify that the Admin is acting on behalf of a client.

#### Mobile & Field Optimization

The **Guard View** is a specific UX module designed for high-glare, outdoor environments.

* **High Contrast:** Large buttons and high-contrast text make it readable on mobile devices in sunlight.
* **Integrated Scanning:** The UI provides a one-tap access to the device camera for scanning QR codes, eliminating the need for manual typing of long serial numbers.
