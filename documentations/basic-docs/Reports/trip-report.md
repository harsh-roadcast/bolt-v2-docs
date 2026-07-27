## Trip Report

Use this report when you need to analyse individual journeys completed by vehicles.

### What this report shows

One row per journey. A journey is a single movement from where the vehicle set off to where it finally came to rest - not the whole day, and not every individual stop within it.

#### Questions it can answer

- How many trips did a vehicle complete?
- When did each trip begin and end?
- What distance was covered?
- How long did the trip take?
- Where did the vehicle stop?
- How much idle time occurred during the trip?

#### Primary data level

**Trip** - Level 2 in the report hierarchy. Broader than Events and Positions, narrower than Summary.

### Commonly used columns

| Column                        | What it tells you                      | Identifying? |
|-------------------------------|----------------------------------------|--------------|
| **Trip ID**                   | Unique reference for the journey       | Yes          |
| **Vehicle ID**                | Which vehicle made the journey         | Yes          |
| Start time / End time         | When the journey began and ended       | \-           |
| Start location / End location | Where it began and ended               | \-           |
| Distance                      | Kilometres covered                     | \-           |
| Duration                      | Total elapsed time                     | \-           |
| Idle time                     | Time spent stationary with ignition on | \-           |
| Stop count                    | Number of stops within the journey     | \-           |

> **Important:** Keep at least one identifying column - Trip ID or Vehicle ID - or the report cannot be generated. See Selecting and managing columns.

### Recommended filters

- **Date and time** - always. Start with a single day.
- **Vehicle** or **vehicle group** - narrow to the fleet section you care about.
- **Driver** - if you are reviewing a person rather than an asset.

> **Needs product confirmation:** Trip status, minimum distance and minimum duration filters appear in the interface but their exact behaviour is not documented in the supplied material. Confirm before relying on them.

### Example: the late route

**The situation.** A distribution vehicle running Bhiwandi. Then Kalyan is consistently arriving 40 minutes late. The driver says traffic. Dispatch suspects a long lunch stop.

1.  ##### Select base reports

    **Trip**, then add **Stop and Idle** - its companion.

2.  ##### Select the asset

    MH12-AB-1234.

3.  ##### Set the date range

    The last two weeks, so the pattern shows rather than one bad day.

4.  ##### Group by

    Date, so each day's trips sit together.

5.  ##### Read the result

    If the trips themselves are the same length but idle time spikes at 13:00 every day, dispatch was right. If the trip duration itself has grown, the driver was.

### Reports it combines with

| Combine with            | Result                                                    |
|-------------------------|-----------------------------------------------------------|
| Confirmed Summary       | Trips nest under the summary row for that vehicle or day. |
| Confirmed Stop and Idle | Every stop and idle spell inside each trip.               |
| Confirmed Events        | Events nest under the trip they occurred in.              |
| Confirmed Event IVMS    | As above, in IVMS format.                                 |
| Confirmed Positions     | Raw GPS points attached to each trip. Large output.       |
| MVI                     | MVI always runs alone.                                    |

### Limitations

- Trip + Positions produces a very large file. Keep the date range short.
- A trip is only recorded if the device reported through the journey. Gaps in device data appear as gaps in trips, not as errors.

------------------------------------------------------------------------

