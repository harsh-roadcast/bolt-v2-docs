## Events Report

Every flagged driving behaviour - harsh braking, overspeed, harsh acceleration - with when, where and how fast.

> **Note:** Events and Event IVMS both sit at Level 3. They are two formats of the same level of detail. Choose the one your team actually reads.

### What this report shows

One row per event the system flagged. An event is a moment, not a period - it has a timestamp, not a duration.

#### One row means

**One event. One harsh brake, one overspeed instance, one harsh turn.**

### Questions it answers

- Which drivers are braking hard, and where?
- Is overspeeding concentrated on one route?
- Did behaviour improve after coaching?
- Which vehicle triggered the most events last week?
- Do events cluster at a particular junction - and if so, is that a driver problem or a road problem?

### Primary data level

**Level 3.** Sits beneath Trip and Summary, above Positions.

> **Tip:** Events on their own tell you what. Events nested under Trip tell you what, during which journey - which is usually the more actionable question. Trip + Events is one of the most useful combinations in BOLT.

### Commonly used columns

| Column         | What it tells you                                  | Identifying? |
|----------------|----------------------------------------------------|--------------|
| **Event ID**   | Unique reference for the event                     | Yes          |
| **Vehicle ID** | Which vehicle                                      | Yes          |
| **Timestamp**  | Exactly when it happened                           | Yes          |
| Event type     | Harsh braking, overspeed, harsh acceleration, etc. | \-           |
| Location       | Where it happened                                  | \-           |
| Speed          | Speed at the moment of the event                   | \-           |
| Driver         | Who was driving                                    | \-           |
| Severity       | How serious                                        | \-           |

Identifying columns are marked. At least one from the primary report must stay selected.

> **Important:** If this report is your primary, you must keep at least one identifying column or the report cannot be generated. See Selecting and managing columns.

### Recommended filters

- **Date and time** - a week is a good behaviour window.
- **Driver** - this is usually a person question, not an asset question.
- **Event type** - needs confirmation. If available, filter to one behaviour at a time.
- **Vehicle group**.

> **Needs product confirmation:** Event type is listed as a possible filter in the brief but its behaviour and the full list of event types are not confirmed. See Open questions.

### Worked example

**The situation.** One driver is triggering three times the harsh-braking events of anyone else. HR wants a coaching conversation. You want to be sure it is actually him before you have it.

1.  ##### Select Trip + Events

    Not Events alone. You need to know which journeys the events happened in.

2.  ##### Select the driver

    Filter by driver, not vehicle - he may drive several.

3.  ##### Set the range to a month

    Enough that it is a pattern, not a bad week.

4.  ##### Group by event type

    Separate harsh braking from overspeed.

5.  ##### Look at where the events cluster

    **Here is the thing worth checking.** If 80% of his harsh braking is on one route, at one junction, at the same time of day - that is not a bad driver. That is a bad junction, and every driver on that route would do the same. Run the same report for a second driver on the same route before you have the conversation.

**What you learn.** Events tell you what the vehicle did. They do not tell you whether it was the driver's fault. Nesting events under trips, and comparing across drivers on the same route, is what turns the data into a fair judgement.

### Combines with

| Report               | Allowed?           | What you get                                                                   |
|----------------------|--------------------|--------------------------------------------------------------------------------|
| **Trip**             | Confirmed Yes      | Events nest under the journey they happened in. The most useful pairing.       |
| **Summary**          | Confirmed Yes      | Events roll up under the summary row.                                          |
| **Positions**        | Confirmed Yes      | Shows exactly where each event occurred.                                       |
| **Incident Summary** | No                 | **Confirmed restriction.** Incompatible record structures.                     |
| **Stop and Idle**    | No                 | **Confirmed restriction.** Incompatible record structures.                     |
| **Event IVMS**       | Needs confirmation | Both occupy Level 3. Whether they can coexist is an open question - see below. |
| **MVI**              | No                 | MVI always runs alone.                                                         |

### Limitations

- An event is a flag, not a verdict. Context - the route, the junction, the traffic - decides whether it means anything.
- Cannot be combined with Stop and Idle or Incident Summary. Two of the four confirmed restrictions.

> **Needs product confirmation:** Whether Events and Event IVMS can both be selected is not stated in the brief. Both sit at Level 3 and the "one primary report per level" rule suggests they should block each other - but this is not confirmed. The compatibility explorer currently allows both. Logged in Open questions as item 13.

------------------------------------------------------------------------

