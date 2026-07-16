## Report Catalogue

Eight report types. Each one answers a different kind of question. Here is all of them, side by side.

### Every report type

| Report | Level | Description |
|--------|-------|-------------|
| [Summary](#summary-report) | 1 | **How did the fleet perform overall?** Rolled-up totals per vehicle or per day - distance, running time, idle time, event counts. |
| [Incident Summary](#incident-summary-report) | Companion to Summary | **How many incidents, and where?** Incident totals sitting alongside summary figures. |
| [Trip](#trip-report) | 2 | **What journeys did each vehicle complete?** One row per journey - start, end, distance, duration, stops, idle. |
| [Stop and Idle](#stop-and-idle-report) | Companion to Trip | **Where is time being lost?** Every stop and idle spell with location and duration. |
| [Events](#events-report) | 3 | **What driving behaviour was flagged?** Harsh braking, overspeed, harsh acceleration and other alerts. |
| [Event IVMS](#event-ivms-report) | 3 | **What do the in-vehicle monitoring events show?** IVMS-standard event records at the same level as Events. |
| [Positions](#positions-report) | 4 | **Exactly where was the vehicle, second by second?** Raw GPS position records - the most detailed level available. |
| [MVI](#mvi-report) | Standalone | **What does the vehicle inspection record say?** Motor vehicle inspection data. Always generated on its own. |

> **Note:** Only Trip has a full page written so far - it is the worked example for the report-page template. The remaining seven follow the identical structure and are queued for publication.

### Detail level at a glance

| Report           | Rows you'd get                             | Primary data level |
|------------------|--------------------------------------------|--------------------|
| Summary          | 1 row - the whole day                      | Vehicle / day      |
| Incident Summary | 1 row - incident totals                    | Vehicle / day      |
| Trip             | 6 rows - one per journey                   | Trip               |
| Stop and Idle    | 14 rows - every stop and idle spell        | Stop / idle record |
| Events           | 23 rows - one per flagged event            | Event              |
| Event IVMS       | 23 rows - IVMS-standard event records      | Event              |
| Positions        | ~8,600 rows - a GPS ping every few seconds | Position           |
| MVI              | 1 row - the inspection record              | Inspection         |

One day of one vehicle, seen through each report

> **Warning:** Positions is enormous. Ask for one vehicle and one day, not thirty vehicles and a month - you will hit the record limit and the report will fail.

### What combines with what

Reports sit at levels, and a custom report has to read top-down. The [hierarchy page](#report-hierarchy-and-compatibility) explains why, and includes an explorer you can click through.

| Report           | Level                | Combines with                                         |
|------------------|----------------------|-------------------------------------------------------|
| Summary          | 1                    | Trip, Events, Event IVMS, Positions, Incident Summary |
| Incident Summary | Companion to Summary | Summary                                               |
| Trip             | 2                    | Summary, Events, Event IVMS, Positions, Stop and Idle |
| Stop and Idle    | Companion to Trip    | Summary, Trip, Positions                              |
| Events           | 3                    | Summary, Trip, Positions                              |
| Event IVMS       | 3                    | Summary, Trip, Positions                              |
| Positions        | 4                    | Everything except MVI                                 |
| MVI              | Standalone           | Nothing - always runs alone                           |

------------------------------------------------------------------------

