## MVI Report

Motor vehicle inspection records. The only report in BOLT that always runs completely on its own.

> **Error:** MVI cannot be combined with any other base report. Select it and your selection limit drops to one - everything else is cleared. This is not a bug and there is no way around it. If you need inspection data and trip data, that is two reports.

### What this report shows

Vehicle inspection records - what was checked, when, by whom, and what was found.

#### One row means

**One inspection.**

### Questions it answers

- When was this vehicle last inspected?
- Which vehicles are overdue?
- What defects were found, and were they fixed?
- Can we evidence our inspection compliance?

### Primary data level

**Standalone.** MVI sits outside the hierarchy entirely. It has no level, no parent and no children.

> **Note:** MVI is separate because inspection records are not fleet-movement records. A trip has a start, an end and a distance. An inspection has a date, a checklist and an outcome. There is no sensible way to nest one inside the other, so BOLT does not pretend otherwise.

### Commonly used columns

| Column              | What it tells you           | Identifying? |
|---------------------|-----------------------------|--------------|
| **Vehicle ID**      | Which vehicle was inspected | Yes          |
| **Inspection date** | When                        | Yes          |
| Inspector           | Who carried it out          | \-           |
| Result              | Pass, fail, advisory        | \-           |
| Defects found       | What was wrong              | \-           |

Identifying columns are marked. At least one from the primary report must stay selected.

> **Important:** If this report is your primary, you must keep at least one identifying column or the report cannot be generated. See Selecting and managing columns.

### Recommended filters

- **Date and time** - the inspection period.
- **Vehicle** or **vehicle group**.

> **Needs product confirmation:** The full MVI column set, the result values and the defect classification are not specified in the supplied material. Confirm before treating this table as complete.

### Worked example

**The situation.** An audit is scheduled. You need to evidence that every vehicle in the fleet has a current inspection record.

1.  ##### Select MVI

    On its own. It will not let you do otherwise - every other option greys out the moment you pick it.

2.  ##### Select the whole fleet

    Every vehicle.

3.  ##### Set the range to cover the required inspection interval

    If inspections are six-monthly, run the last six months.

4.  ##### Group by vehicle

    So each vehicle's inspection history sits together.

5.  ##### Look for the vehicles that are not in the report

    **This is the important part.** A vehicle with no inspection in the period produces no row. The finding is the *absence* - so cross-check the output against your full vehicle list. The report cannot tell you about a record that does not exist.

**What you learn.** MVI is the one report where the useful answer is often what is missing rather than what is present. Read it against your asset list, not on its own.

### Combines with

| Report               | Allowed? | What you get       |
|----------------------|----------|--------------------|
| **Summary**          | No       | MVI is standalone. |
| **Incident Summary** | No       | MVI is standalone. |
| **Trip**             | No       | MVI is standalone. |
| **Stop and Idle**    | No       | MVI is standalone. |
| **Events**           | No       | MVI is standalone. |
| **Event IVMS**       | No       | MVI is standalone. |
| **Positions**        | No       | MVI is standalone. |

### Limitations

- Cannot be combined with anything. Selecting it clears your existing selection.
- A missing inspection produces no row. Absence of a record is not evidence of compliance - read the output against your asset list.

> **Replace confirmation:** Selecting MVI will remove all other reports from this selection. MVI must be generated on its own. Do you want to continue?

------------------------------------------------------------------------

