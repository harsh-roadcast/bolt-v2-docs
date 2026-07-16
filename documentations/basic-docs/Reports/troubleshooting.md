## Troubleshooting

Fourteen things that go wrong, and how to fix each one without contacting support.

### Fourteen common problems

| Problem                                       | Possible cause                                                                                                   | What to do                                                                                                                            | Contact support if...                                                               |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| **The report contains no data**               | The date range has no activity; the vehicle wasn't reporting; a filter is too narrow.                            | Widen the date range to a week. Remove filters one at a time. Confirm in Live Tracking that the vehicle was reporting on those dates. | If the vehicle was demonstrably moving and reporting and the report is still empty. |
| **A vehicle is missing from the report**      | It wasn't selected; it isn't in the group you picked; you don't have access to it; it sent no data in the range. | Check the asset selection. If you used a group, check the vehicle is in it. Check Live Tracking for device activity.                  | If the vehicle is selected, reporting, and still absent.                            |
| **Expected columns aren't available**         | The column belongs to a base report you haven't selected.                                                        | Add the base report that owns the column. Column source labels tell you which report each one comes from.                             | If the column is listed in the source report but does not appear.                   |
| **A report type is disabled**                 | It can't be combined with what you've already selected, or you've hit the four-report limit.                     | Hover the disabled option for the reason. Use the [compatibility explorer](#report-hierarchy-and-compatibility) to see the rules.     | Rarely - this is working as designed.                                               |
| **Generation is taking longer than expected** | Wide date range; many vehicles; Positions selected; a busy queue.                                                | Leave it - it will finish. Next time, narrow the range or drop Positions.                                                             | If it has been generating for hours with no change.                                 |
| **Generation failed**                         | A configuration problem, or the result exceeded the record limit.                                                | Narrow the date range. Reduce vehicles. Remove Positions if it is in the selection. Try again.                                        | If it fails twice with a narrow, simple configuration.                              |
| **The download link expired**                 | The report passed its retention window and the file was removed.                                                 | Regenerate with the same configuration. If you need it regularly, schedule it instead.                                                | No need - regenerate.                                                               |
| **A scheduled report wasn't received**        | The schedule is paused; the recipient address is wrong; the run produced no data; it went to spam.               | Check the schedule status and Last run. Check the recipient list. Check spam.                                                         | If Last run says it succeeded and the recipient still has nothing.                  |
| **A recipient email is invalid**              | A typo, or the address was rejected on save.                                                                     | Re-enter the address. Save. The schedule validates it.                                                                                | No need.                                                                            |
| **The mobile table is hard to read**          | Too many columns for a phone screen.                                                                             | Scroll horizontally. Better: duplicate the template on web and cut it to the columns that matter.                                     | No need.                                                                            |
| **Data doesn't match the date range**         | Timezone. The report was generated in a different timezone from the one you're reading it in.                    | Check the timezone on the report or schedule. "Yesterday" in IST is not "yesterday" in UTC.                                           | If timezones match and the data is still shifted.                                   |
| **You don't have permission**                 | Your role doesn't include the report action you're attempting.                                                   | Ask your administrator. See [Permissions and access](#permissions-and-access).                                                        | Your administrator handles this, not support.                                       |
| **A saved template has changed**              | Someone edited it. Templates are shared.                                                                         | Check the template's last-updated date. Reports generated before that used the previous configuration.                                | If nobody edited it and it still changed.                                           |
| **Two reports can't be combined**             | One of the four confirmed restrictions applies.                                                                  | Generate them separately. See [hierarchy and compatibility](#report-hierarchy-and-compatibility).                                     | No need - this is intended behaviour.                                               |

Find the symptom in the left column.

### Before you contact support

1.  ##### Narrow it down

    Run the same report for one vehicle, for one day. If that works, the problem is scale, not configuration.

2.  ##### Simplify the selection

    Drop to a single base report. If it works, one of the combinations was the issue.

3.  ##### Check the vehicle is reporting

    If Live Tracking shows nothing, Reports will show nothing. That is a device problem, not a report problem.

4.  ##### Note the details

    Report type, date range, vehicle, timezone, and the exact status or message. Support will ask.

> **Error:** Still stuck? Contact Roadcast Support with the configuration you used and the status you saw. A screenshot of the failed report row saves a round trip.

------------------------------------------------------------------------

