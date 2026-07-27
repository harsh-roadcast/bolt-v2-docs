## Positions Report

Raw GPS. Every ping the device sent. The most detailed report in BOLT - and the easiest one to misuse.

> **Warning:** Read this before you run it. Positions produces roughly 8,000-10,000 rows per vehicle per day. Ten vehicles for a month is around 2.7 million rows. That report will fail, and you will have waited a long time to find out. Start with one vehicle, one day.

### What this report shows

Every position record the device transmitted - latitude, longitude, speed, heading, timestamp. This is the underlying data everything else in BOLT is built from.

#### One row means

**One GPS ping. Typically one every few seconds while the vehicle is moving.**

### Questions it answers

- Exactly where was this vehicle at 14:32 last Tuesday?
- The customer says we never arrived. Did we?
- What route did the driver actually take?
- Was the vehicle inside the customer's yard, or parked outside it?
- Reconstruct the minute before an incident, second by second.

### Primary data level

**Level 4 - the most detailed level.** Nothing sits beneath Positions.

> **Important:** Use Positions when you need to prove something. Not to explore, not to browse - to settle a factual dispute where the exact location at an exact time is the answer. For anything less specific, a higher-level report will serve you better and finish faster.

### Commonly used columns

| Column               | What it tells you              | Identifying? |
|----------------------|--------------------------------|--------------|
| **Timestamp**        | Exactly when the ping was sent | Yes          |
| **Vehicle ID**       | Which vehicle                  | Yes          |
| Latitude / Longitude | The coordinates                | \-           |
| Location             | The address, where resolvable  | \-           |
| Speed                | Speed at that instant          | \-           |
| Heading              | Direction of travel            | \-           |
| Ignition             | On or off                      | \-           |

Identifying columns are marked. At least one from the primary report must stay selected.

> **Important:** If this report is your primary, you must keep at least one identifying column or the report cannot be generated. See Selecting and managing columns.

### Recommended filters

- **Date and time** - **one day. Genuinely.** Narrow to a time window if you can.
- **Vehicle** - one. Not a group.
- **Geofence** - needs confirmation. If available, this is the filter that makes Positions manageable: show only pings inside the customer's yard.

> **Needs product confirmation:** A geofence filter would transform this report - "was the vehicle inside the yard" becomes a two-row answer instead of a ten-thousand-row one. The brief lists Geofence as a possible filter but does not confirm it. This is the single most valuable unconfirmed filter in the module.

### Worked example

**The situation.** A customer is refusing to pay for a delivery. They say the vehicle never arrived on 8 July. The driver insists he was there for twenty minutes. There is money on this.

1.  ##### Select Positions alone

    No Trip, no Summary. You want the raw record, unmediated.

2.  ##### Select the one vehicle

    MH12-AB-1234. Only that one.

3.  ##### Set the range to 8 July, and narrow the time window

    If the delivery was scheduled for the afternoon, run 12:00-18:00, not the whole day. Ten thousand rows becomes two thousand.

4.  ##### Generate, and read the coordinates against the delivery address

    Speed 0, ignition off, coordinates at the customer's gate, 14:12 to 14:31. Nineteen minutes, stationary, at their address.

5.  ##### That is the answer

    It is not an opinion, an estimate or a system-generated flag. It is where the vehicle physically was, recorded second by second at the time it happened. This is the only report in BOLT that produces evidence of that quality - and it is precisely why it exists.

**What you learn.** Positions is the court of last resort. Slow, enormous, and completely unarguable. Every other report in BOLT is a summary of this one.

### Combines with

| Report            | Allowed?      | What you get                                         |
|-------------------|---------------|------------------------------------------------------|
| **Trip**          | Confirmed Yes | GPS trace per journey. Large.                        |
| **Events**        | Confirmed Yes | Exactly where each event occurred.                   |
| **Event IVMS**    | Confirmed Yes | As above.                                            |
| **Stop and Idle** | Confirmed Yes | Stops with the raw trace around them.                |
| **Summary**       | Confirmed Yes | Allowed. Rarely a good idea - the file will be vast. |
| **MVI**           | No            | MVI always runs alone.                               |

### Limitations

- **Size.** This is the whole limitation. Everything else about Positions is a consequence of it.
- A ping is only recorded if the device was reporting. Tunnels, dead zones and device faults appear as gaps - a gap is not proof the vehicle was not there.
- Coordinates are accurate to within a few metres, not centimetres. "Inside the gate or ten metres outside it" is at the edge of what GPS can honestly answer.

> **Too many records:** This configuration returns too many records. Narrow the date range or reduce the number of vehicles.

------------------------------------------------------------------------

