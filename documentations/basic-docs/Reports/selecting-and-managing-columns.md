## Selecting and Managing Columns

Columns are where a custom report earns its keep - and where most confusion lives. This page removes it.

### What happens when you change something

| You do this                                                  | BOLT does this                                                                                                    |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **Add a compatible secondary report**                        | Its default columns are appended to your current selection. What you already picked stays.                        |
| **Change the primary (highest-level) report**                | Incompatible columns are removed. The default columns for the new primary are loaded in.                          |
| **Remove every column belonging only to a secondary report** | That secondary report stops contributing data to the generated output. It is effectively no longer in the report. |
| **Remove the last identifying column of the primary report** | Blocked. The report cannot be generated without one.                                                              |

> **Important:** Identifying columns are the ones that tell you which record a row is: Vehicle ID, Trip ID, Timestamp, Event ID. At least one from the primary report must stay selected.

> **Validation:** Keep at least one identifying column from the primary report.

### What you can do with columns

| Action                  | Notes                                                                                                |
|-------------------------|------------------------------------------------------------------------------------------------------|
| **Search**              | Type to filter the available column list. Useful once a four-report selection gives you a long list. |
| **Add**                 | From the available list into the selected list.                                                      |
| **Remove**              | Anything except the last identifying column of the primary report.                                   |
| **Reorder**             | Drag. Order carries through to preview, file and schedule.                                           |
| **Rename (alias)**      | Give the column the name your team uses. The alias is what appears in the output.                    |
| **Restore defaults**    | Resets to the default column set for your current base reports.                                      |
| **Identify the source** | Every column carries a label - Summary, Trip, Stop and Idle, Events, Positions.                      |

> **Needs product confirmation:** Mandatory columns beyond the identifying-column rule, duplicate-column handling, and any unsupported column pairings are not fully specified in the supplied material.

### Source labels

When four reports contribute columns, "Duration" is ambiguous - trip duration or idle duration? The source label resolves it. Read the label before you add the column.

### Common mistakes

- **Adding a report, then wondering why the file is unchanged.** You removed all its columns. It is contributing nothing. Add one back.
- **Renaming a column, then not recognising it in the schedule.** Aliases carry through everywhere. That is the point.
- **Changing the primary report late, losing careful column work.** Decide the base reports first.

------------------------------------------------------------------------

