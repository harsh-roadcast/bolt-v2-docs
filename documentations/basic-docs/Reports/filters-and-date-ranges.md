## Filters and Date Ranges

Filters narrow the rows. The date range is the one that matters most.

### The date range

Every report needs one. It determines how long generation takes, how large the file is, and whether the report succeeds at all.

| Base report         | Start with                                      |
|---------------------|-------------------------------------------------|
| Summary             | A month. It is rolled up - it stays small.      |
| Trip                | A week.                                         |
| Stop and Idle       | A week.                                         |
| Events / Event IVMS | A week.                                         |
| Positions           | **One day, one vehicle.** Then widen carefully. |

A sensible starting range, by report

> **Warning:** Report data not matching your date range? Check the timezone the report was generated in. A report run in a different timezone shifts the boundary of "yesterday" by hours.

### Available filters

Which filters appear depends on the base reports you selected. Selecting Events surfaces event-type filters; selecting Trip surfaces trip filters.

| Filter          | Status                     |
|-----------------|----------------------------|
| Date and time   | Confirmed                  |
| Vehicle         | Confirmed                  |
| Vehicle group   | Confirmed                  |
| Driver          | Confirmed                  |
| Driver group    | Needs product confirmation |
| Device          | Needs product confirmation |
| Geofence        | Needs product confirmation |
| Event type      | Needs product confirmation |
| Trip status     | Needs product confirmation |
| Ignition status | Needs product confirmation |
| Speed           | Needs product confirmation |
| Duration        | Needs product confirmation |

> **Needs product confirmation:** The filters marked above appear in the supplied interface material but their behaviour, operators and interaction with base-report selection are not specified. They are listed here for completeness, not as confirmed product behaviour. See Open questions.

### Runtime filters

A saved template can be run with a different date range or asset selection without editing the template itself. That is a **runtime filter** - it applies to this run only and does not change what is saved. It is how a template stays useful week after week, and it is what makes templates usable from mobile.

> **Note:** Runtime filters cannot add columns or change grouping. Structural changes mean editing the template on web.

------------------------------------------------------------------------

