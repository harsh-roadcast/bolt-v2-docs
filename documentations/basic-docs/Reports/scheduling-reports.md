## Scheduling Reports

Stop generating the same report by hand every Monday. Schedule it once.

### What a schedule does

A schedule runs a saved report or template automatically and delivers the result to a list of recipients. It is not a report - it *produces* reports.

> **Permission required:** Creating and editing schedules requires the schedule permission. Without it, you can view schedules but not change them.

### Setting one up

<figure><img src="../../.gitbook/assets/web_add_schedule.png" alt=""><figcaption></figcaption></figure>

*Choose the organization, recipients, frequency, delivery time, and file format before saving the schedule.*

| Field                  | What to enter                            | Notes                                       |
|------------------------|------------------------------------------|---------------------------------------------|
| **Schedule name**      | Something a recipient would recognise    | "Weekly idle - North fleet", not "Report 3" |
| **Report or template** | The saved configuration to run           | Must exist first                            |
| **Frequency**          | One time, Daily, Weekly, Monthly, Custom | Custom behaviour needs confirmation         |
| **Start date**         | When it begins                           | \-                                          |
| **End date**           | When it stops                            | Optional - leave blank to run indefinitely  |
| **Time**               | When it runs                             | Pick a time after the data has settled      |
| **Timezone**           | Which timezone the time refers to        | Matters more than people expect             |
| **Recipients**         | Email addresses                          | Validated when you save                     |
| **File format**        | The export format                        | Available formats need confirmation         |

> **Needs product confirmation:** The exact frequency options, the definition of "Custom", and the supported file formats are listed in the supplied material without behavioural detail. Confirm before documenting further.

> **Tip:** Schedule a daily report for 07:00 rather than 00:05. Yesterday's data has settled by then, and the report is waiting when people arrive.

### Managing a schedule

<figure><img src="../../.gitbook/assets/web_view_schedules.png" alt=""><figcaption></figcaption></figure>

*Review the schedules attached to a report template and their next run time.*

| Field / action | Meaning                                                       |
|----------------|---------------------------------------------------------------|
| **Active**     | Running as configured.                                        |
| **Paused**     | Will not run until resumed. Configuration is kept.            |
| **Next run**   | When it fires next.                                           |
| **Last run**   | When it last fired, and whether that run succeeded.           |
| **Edit**       | Change frequency, recipients, format. Applies to future runs. |
| **Pause**      | Stop temporarily - for a holiday shutdown, say.               |
| **Resume**     | Restart a paused schedule.                                    |
| **Delete**     | Removes the schedule. Reports it already produced remain.     |

> **Tip:** Going into a shutdown period? Pause the schedule rather than deleting it. You will not have to rebuild it in January.

### Recipients and empty runs

Recipient addresses are validated when you save the schedule. An invalid address is rejected at that point rather than failing silently every week.

> **Invalid recipient:** This email address isn't valid. Check the spelling and try again.

> **Needs product confirmation:** What happens when a scheduled run produces no data - whether an empty file is sent, a notice is sent, or the run is skipped - is not specified in the supplied material.

> **Scheduled run - no data (proposed copy):** Your scheduled report ran but no data matched the configuration. Nothing was sent. Review the schedule's date range and filters.

### Schedule states

> **Created:** Schedule created. The first report runs on 20 July 2026 at 07:00 IST.

> **Paused:** Schedule paused. It won't run again until you resume it.

> **Deleted:** Schedule deleted. Reports it already generated are still available.

> **Empty state - no schedules:** No schedules yet. Schedule a saved report to have it generated and sent automatically.

------------------------------------------------------------------------

