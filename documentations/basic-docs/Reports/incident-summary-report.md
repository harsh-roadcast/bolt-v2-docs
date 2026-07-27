## Incident Summary Report

Incident totals, sitting alongside your summary figures. A companion to Summary, not a level of its own.

> **Important:** Incident Summary is a companion. It sits at Level 1 beside Summary rather than beneath it. It is the one report with the most restrictions - read the Combines with section carefully before you build with it.

### What this report shows

Rolled-up incident counts for the period, in the same shape as Summary so the two read together as one table.

#### One row means

**One vehicle, one period - with incident totals rather than movement totals.**

### Questions it answers

- How many incidents did we have this quarter?
- Which vehicles are involved in incidents most often?
- Is the incident rate going up or down?
- Which depot has the worst record?
- Did the safety intervention in April actually work?

### Primary data level

**Level 1 - companion to Summary.** It does not have children. Nothing nests under Incident Summary.

> **Warning:** Because Incident Summary is a companion rather than a level, it cannot sit above Events, Event IVMS or Stop and Idle. Those three are the confirmed restrictions. See Hierarchy and compatibility.

### Commonly used columns

| Column         | What it tells you                | Identifying? |
|----------------|----------------------------------|--------------|
| **Vehicle ID** | Which vehicle                    | Yes          |
| **Date**       | The period covered               | Yes          |
| Incident count | How many incidents in the period | \-           |
| Incident type  | The category of incident         | \-           |
| Severity       | How serious                      | \-           |

Identifying columns are marked. At least one from the primary report must stay selected.

> **Important:** If this report is your primary, you must keep at least one identifying column or the report cannot be generated. See Selecting and managing columns.

### Recommended filters

- **Date and time** - a quarter is a reasonable window for incident trends.
- **Vehicle group** - compare depots or regions.
- **Vehicle** - for a single-asset investigation.

> **Needs product confirmation:** The full incident column set, incident type values and severity scale are not enumerated in the supplied material. The columns above are the ones referenced in the brief. Confirm the complete list before treating this table as exhaustive.

### Worked example

**The situation.** The safety committee wants to know whether the driver-coaching programme launched in April made any difference.

1.  ##### Select Summary + Incident Summary

    Two Level 1 reports, sitting side by side. This is the classic companion pairing.

2.  ##### Select the whole fleet

    This is a programme-level question.

3.  ##### Set the range to January through July

    You need before and after.

4.  ##### Group by date

    Month by month.

5.  ##### Read the incident count against distance

    This is why you added Summary. Incidents alone are misleading - if the fleet drove 30% further, more incidents is not a worse record. Incidents *per kilometre* is the honest number, and you can only calculate it because Summary is in the same table.

**What you learn.** Incident Summary is far more useful with Summary beside it than on its own. Raw incident counts without distance context are one of the easiest ways to reach a wrong conclusion in fleet management.

### Combines with

| Report            | Allowed?      | What you get                                                                    |
|-------------------|---------------|---------------------------------------------------------------------------------|
| **Summary**       | Confirmed Yes | The intended pairing. Incident totals beside movement totals.                   |
| **Trip**          | Confirmed Yes | Trips nest under Summary. Incident Summary stays alongside.                     |
| **Events**        | No            | **Confirmed restriction.** Incompatible record structures. Generate separately. |
| **Event IVMS**    | No            | **Confirmed restriction.** Same reason.                                         |
| **Stop and Idle** | No            | **Confirmed restriction.** Same reason.                                         |
| **Positions**     | Confirmed Yes | Allowed.                                                                        |
| **MVI**           | No            | MVI always runs alone.                                                          |

### Limitations

- Three of the four confirmed combination restrictions in BOLT involve this report. If an option greys out unexpectedly, Incident Summary is usually the reason.
- Incident counts without a distance or time denominator are misleading. Pair with Summary.

------------------------------------------------------------------------

