## Summary Report

The broadest view in BOLT. Everything a vehicle did in a period, rolled into a single line.

> **Note:** Summary sits at Level 1 - the top of the hierarchy. Whenever you include it in a custom report, it becomes the primary and everything else nests underneath it.

### What this report shows

Totals. Not journeys, not events, not GPS points - the aggregate of all of them. If a vehicle made six trips, stopped fourteen times and triggered twenty-three events, Summary gives you one row that adds all of that up.

#### One row means

**One vehicle, one period (typically one day).**

### Questions it answers

- How far did the fleet run last month?
- Which vehicle is doing the most kilometres?
- How much time are we losing to idle, across the whole fleet?
- How many events did each vehicle trigger?
- Is utilisation improving month on month?
- Which vehicles barely moved?

### Primary data level

**Vehicle / period.** Level 1 - the broadest level there is. Every other base report can nest beneath it.

> **Tip:** Summary is the right starting point for almost any question that begins "overall..." or "across the fleet...". If you find yourself scrolling through a Trip report adding up distances by hand, you wanted Summary.

### Commonly used columns

| Column         | What it tells you                | Identifying? |
|----------------|----------------------------------|--------------|
| **Vehicle ID** | Which vehicle the row is about   | Yes          |
| **Date**       | The period the totals cover      | Yes          |
| Total distance | Kilometres covered in the period | \-           |
| Running time   | Time spent actually moving       | \-           |
| Idle time      | Stationary, ignition on          | \-           |
| Stopped time   | Stationary, ignition off         | \-           |
| Trip count     | How many journeys were made      | \-           |
| Event count    | How many events were triggered   | \-           |
| Max speed      | Highest speed recorded           | \-           |
| Average speed  | Mean speed across the period     | \-           |

Identifying columns are marked. At least one from the primary report must stay selected.

> **Important:** If this report is your primary, you must keep at least one identifying column or the report cannot be generated. See Selecting and managing columns.

### Recommended filters

- **Date and time** - a month is comfortable here. Summary stays small because it is rolled up.
- **Vehicle group** - compare the North fleet against the South.
- **Vehicle** - if you are investigating one asset.

### Worked example

**The situation.** Month-end review. The fleet did 42,000 km, which sounds fine. But fuel cost is up 11% and nobody can explain why.

1.  ##### Select Summary alone

    No other base report. You want totals, not detail.

2.  ##### Select the whole fleet

    All vehicles. This is a fleet-level question.

3.  ##### Set the range to last month

    Summary handles a month without complaint.

4.  ##### Group by vehicle

    So each vehicle gets its own subtotal.

5.  ##### Turn on Sum for idle time

    And enable the grand total - it is off by default.

6.  ##### Read the idle column

    If three vehicles account for 60% of fleet idle time, you have found your 11%. Now run a [Stop and Idle](#stop-and-idle-report) report on those three to see *where*.

**What you learn.** Summary tells you **which** vehicle has the problem. It never tells you **why**. That is what the lower levels are for - and that is the whole logic of the hierarchy.

### Combines with

| Report               | Allowed?      | What you get                                                                   |
|----------------------|---------------|--------------------------------------------------------------------------------|
| **Incident Summary** | Confirmed Yes | Incident totals sit beside the summary totals. Same level - a companion.       |
| **Trip**             | Confirmed Yes | Every journey nests under its summary row.                                     |
| **Stop and Idle**    | Confirmed Yes | Stops nest beneath. Usually you want Trip in between.                          |
| **Events**           | Confirmed Yes | Events nest under the summary. Add Trip too and they nest under trips instead. |
| **Event IVMS**       | Confirmed Yes | As above, in IVMS format.                                                      |
| **Positions**        | Confirmed Yes | Allowed, but produces an enormous file. Think hard.                            |
| **MVI**              | No            | MVI always runs alone.                                                         |

### Limitations

- Summary hides the story. A vehicle with 4 hours of idle might have had one four-hour breakdown or forty six-minute stops. Summary cannot tell you which - [Stop and Idle](#stop-and-idle-report) can.
- Averages in Summary are already averaged. Do not average them again across vehicles - see the warning in [Grouping and aggregation](#grouping-and-aggregation).

------------------------------------------------------------------------

