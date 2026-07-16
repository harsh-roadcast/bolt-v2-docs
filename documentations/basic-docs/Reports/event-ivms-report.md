## Event IVMS Report

The same event level as Events, formatted to the IVMS standard used in regulated and contractual reporting.

> **Important:** Events or Event IVMS - which do I want? Use Events for internal fleet management. Use Event IVMS when an external party defines the format - a client contract, a regulator, an oil-and-gas or mining customer with IVMS reporting obligations.

### What this report shows

In-Vehicle Monitoring System event records. The same underlying moments as Events, presented in the structure the IVMS standard expects.

#### One row means

**One IVMS event record.**

### Questions it answers

- Can we produce the IVMS report our client contract requires?
- Does our event data meet the reporting standard the regulator expects?
- What do we submit for the quarterly compliance return?

### Primary data level

**Level 3.** The same level as Events - beneath Trip, above Positions.

> **Note:** Because Events and Event IVMS occupy the same hierarchy level, selecting both is an open question - see the note on the Events page. Choose one.

### Commonly used columns

| Column          | What it tells you                          | Identifying? |
|-----------------|--------------------------------------------|--------------|
| **Event ID**    | Unique reference                           | Yes          |
| **Vehicle ID**  | Which vehicle                              | Yes          |
| **Timestamp**   | When it occurred                           | Yes          |
| IVMS event type | The event, classified to the IVMS standard | \-           |
| Location        | Where it occurred                          | \-           |
| Speed           | Speed at the moment of the event           | \-           |
| Driver          | Who was driving                            | \-           |

Identifying columns are marked. At least one from the primary report must stay selected.

> **Important:** If this report is your primary, you must keep at least one identifying column or the report cannot be generated. See Selecting and managing columns.

### Recommended filters

- **Date and time** - usually the contractual reporting period. A month or a quarter.
- **Vehicle group** - often the fleet assigned to a specific client contract.
- **Driver**.

> **Needs product confirmation:** The complete IVMS column set and the IVMS event-type classification list are not specified in the supplied material. Confirm against the PRD before this table is treated as authoritative.

### Worked example

**The situation.** A mining client's contract requires a monthly IVMS event submission. It is due on the 3rd of every month and somebody currently builds it by hand.

1.  ##### Select Trip + Event IVMS

    Trip gives the journey context the submission expects.

2.  ##### Select the vehicle group assigned to that contract

    Not the whole fleet. Only the assets covered by the agreement.

3.  ##### Set the range to the previous calendar month

    And check the timezone - a contractual month boundary is not a place to be casual about it.

4.  ##### Configure the columns the contract specifies

    Rename them with aliases to match the client's expected headers exactly. Do this once.

5.  ##### Save it as a template, then schedule it

    Monthly, on the 2nd, at 06:00, emailed to the client contact and your compliance lead. Nobody builds it by hand again.

**What you learn.** This is the report most worth scheduling. It is recurring, contractual, format-sensitive, and building it by hand every month is exactly the kind of task that eventually gets done late or wrong.

### Combines with

| Report               | Allowed?           | What you get                              |
|----------------------|--------------------|-------------------------------------------|
| **Trip**             | Confirmed Yes      | IVMS events nest under trips.             |
| **Summary**          | Confirmed Yes      | Roll up under summary rows.               |
| **Positions**        | Confirmed Yes      | Exact location of each IVMS event.        |
| **Incident Summary** | No                 | **Confirmed restriction.**                |
| **Stop and Idle**    | No                 | **Confirmed restriction.**                |
| **Events**           | Needs confirmation | Same level. See [Events](#events-report). |
| **MVI**              | No                 | MVI always runs alone.                    |

### Limitations

- Carries the same restrictions as Events - no Stop and Idle, no Incident Summary.
- If the receiving party specifies exact column headers, use column aliases and get them right before you schedule it.

------------------------------------------------------------------------

