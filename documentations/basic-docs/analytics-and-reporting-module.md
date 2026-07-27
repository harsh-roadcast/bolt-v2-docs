# Analytics & Reporting Module

The Reports Module in Bolt V2 is a powerful analytics engine designed for fleet managers and logistics supervisors. It offers a hybrid approach to data visibility: **Standard Reports** for common industry metrics (like Trips and Fuel) and a flexible **Custom Report Builder** that allows you to define your own data structures.

#### 1. The Reports Dashboard

The dashboard is your entry point for all analytics. It is designed with a "Card-Based" layout for quick access to your most important data.

**1.1 Dashboard Organization**

* **Categorization:** Reports are visually separated into "Standard" (system-defined) and "Custom" (user-created) sections.
* **Search & Filter:** Use the global search bar to find specific reports by name, or filter by category (e.g., "Fuel," "Safety").
* **Starring (Favorites):** Click the **Star Icon** on any report card to "Favorite" it. Starred reports automatically float to the top of your dashboard for instant access.

<figure><img src="../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

#### 2. Generating a Report

The platform uses a streamlined **3-Step Generation Flow** to ensure you get exactly the data you need without unnecessary clicks.

**Step 1: Configuration**

Click **"Generate"** on any report card to open the configuration sidebar.

1. **Organization:** Pre-selected to your current active branch.
2. **Device Selection:** Choose specific vehicles or use the "Select All" option for fleet-wide analysis.
3. **Time Range:** Pick a quick filter (Today, Yesterday, Last Week) or define a custom date range.

**Step 2: Processing**

Once you click "Generate," the system begins fetching data. You will see a "Just a Moment" graphic while the query engine processes your request.

**Step 3: Output & Analysis**

The data is rendered in a high-performance table. You can sort columns, paginate through results, and review the metrics directly in the browser.

<figure><img src="../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

#### 3. Custom Report Builder

If the standard reports don't fit your unique operational KPIs, you can build your own.

**3.1 Creating a Custom Report**

1. Click the **"Create Custom Report"** button on the dashboard.
2. **Select Domain:** Choose a base data source (e.g., "Trip Data" or "Fuel Sensor Data").
3. **Column Picker:** Use the **Shuttle Selector** to drag and drop available columns (e.g., "Max Speed," "Idle Time") into your report. You can rearrange their order to match your preference.
4. **Save:** Give your report a name (e.g., "Monday Morning Briefing") and save it. It will now appear as a persistent card on your dashboard.

<figure><img src="../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

#### 4. Exporting & Sharing

Bolt V2 eliminates the need to download files just to email them to a colleague.

* **Download:** Export any generated table as a **CSV** or **Excel (.xlsx)** file for further analysis in external tools.

#### 5. Operational Logic & Edge Cases

| Scenario             | System Behavior                                                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **High Volume Data** | If you select "Last 6 Months" for 10,000 devices, the system may switch to "Asynchronous Mode" and notify you via email when the report is ready. |
| **Zero Data**        | If no vehicles moved during the selected timeframe, the table will display a "No records found" empty state rather than a blank screen.           |
| **Deleted Devices**  | Historical data for deactivated or deleted devices is preserved and will still appear in reports for dates when the device was active.            |

> **Security Note:** Report access is strictly governed by your **Subscription Tier**. Admin users cannot generate reports on client data to maintain privacy.
