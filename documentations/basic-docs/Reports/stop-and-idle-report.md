## Stop and Idle Report

Every stop and every idle spell, with where it happened and how long it lasted. This is the report that finds wasted time.

> **Note:** A stop is stationary with the ignition off. Idle is stationary with the ignition on - the engine running, fuel burning, vehicle going nowhere. The distinction is the entire point of this report.

### What this report shows

One row for every time the vehicle stopped moving - whether the engine was off (a stop) or running (idle). Location, start, end, duration.

#### One row means

**One stop, or one idle spell.**

### Questions it answers

- Where is the vehicle sitting idle, and for how long?
- How much fuel are we burning going nowhere?
- Is the driver taking a 90-minute lunch?
- Why is this route always late - traffic, or dwell time at the customer?
- Which delivery point has the worst turnaround?
- Which vehicles idle most?

### Primary data level

**Level 2 - companion to Trip.** Sits beside Trip, not beneath it.

> **Important:** Idle time costs real money. A truck idling burns roughly 2-3 litres an hour and puts wear on the engine while producing nothing. This is usually the fastest report to a cost saving in the whole module.

### Commonly used columns

| Column                | What it tells you           | Identifying? |
|-----------------------|-----------------------------|--------------|
| **Vehicle ID**        | Which vehicle               | Yes          |
| **Timestamp**         | When the stop or idle began | Yes          |
| Type                  | Stop or Idle                | \-           |
| Location              | Where it happened           | \-           |
| Start time / End time | The window                  | \-           |
| Duration              | How long it lasted          | \-           |
| Driver                | Who was in the vehicle      | \-           |

Identifying columns are marked. At least one from the primary report must stay selected.

> **Important:** If this report is your primary, you must keep at least one identifying column or the report cannot be generated. See Selecting and managing columns.

### Recommended filters

- **Date and time** - a week gives you a pattern rather than an anecdote.
- **Vehicle** or **vehicle group**.
- **Duration** - needs confirmation, but filtering out stops under 2 minutes would remove traffic-light noise.

> **Needs product confirmation:** A minimum-duration filter would make this report substantially more usable - without it, every traffic light appears as a stop. The brief lists Duration as a possible filter but does not confirm it. Flagged in Open questions.

### Worked example

**The situation.** The Bhiwandi. Then Kalyan route is 40 minutes late, every day. The driver says traffic. Dispatch suspects a long lunch. Somebody is wrong.

1.  ##### Select Trip + Stop and Idle

    The companion pairing. Trip gives you the journey; Stop and Idle gives you what happened inside it.

2.  ##### Select MH12-AB-1234

    One vehicle. This is a specific accusation.

3.  ##### Set the range to the last two weeks

    Long enough that a pattern is undeniable and one bad day cannot explain it.

4.  ##### Group by date

    Each day's trips and stops together.

5.  ##### Read the two columns against each other

    **If trip duration is unchanged but a 55-minute stop appears at 13:00 every single day** - dispatch was right. **If trip duration itself has grown by 40 minutes and the stops are unchanged** - the driver was right, and the route genuinely got slower.

**What you learn.** This is the report that settles arguments. Two columns, read side by side, and the answer is not a matter of opinion.

### Combines with

| Report               | Allowed?      | What you get                                                               |
|----------------------|---------------|----------------------------------------------------------------------------|
| **Trip**             | Confirmed Yes | The intended pairing. Every stop inside every journey.                     |
| **Summary**          | Confirmed Yes | Stops roll up under summary rows.                                          |
| **Positions**        | Confirmed Yes | Raw GPS alongside stops. Large output.                                     |
| **Events**           | No            | **Confirmed restriction.** Incompatible record structures. Run separately. |
| **Event IVMS**       | No            | **Confirmed restriction.** Same reason.                                    |
| **Incident Summary** | No            | **Confirmed restriction.** Same reason.                                    |
| **MVI**              | No            | MVI always runs alone.                                                     |

### Limitations

- Without a minimum-duration filter, every traffic light is a stop. Expect noise.
- Stop and Idle cannot be combined with Events - two of the four confirmed restrictions involve this report. If you want driving behaviour *and* dwell time, that is two reports.

> **Conflict message:** Stop and Idle cannot be combined with Events because these reports use incompatible record structures. Generate them separately or remove one of the selected reports.

------------------------------------------------------------------------

