## Choosing the Correct Report

Start from the question you are trying to answer, not from the report names.

### Decision table

| If you need to know...                                 | Use                            | Why                                                                    |
|--------------------------------------------------------|--------------------------------|------------------------------------------------------------------------|
| Total distance, running time and idle across the fleet | **Summary**                    | Rolls everything up. One row per vehicle or per day.                   |
| How many incidents happened, and their totals          | **Summary + Incident Summary** | Incident Summary sits beside Summary at the same level.                |
| What individual journeys a vehicle made                | **Trip**                       | One row per journey - start, end, distance, duration.                  |
| Where time is being lost between journeys              | **Trip + Stop and Idle**       | Stop and Idle is Trip's companion. Gives you every stop with duration. |
| Which drivers are braking hard or overspeeding         | **Events**                     | One row per flagged event, with time, speed and place.                 |
| Behaviour events in IVMS format                        | **Event IVMS**                 | Same level as Events. Choose one or the other, not both.               |
| Exactly where a vehicle was at 14:32 last Tuesday      | **Positions**                  | Raw GPS. The most detailed level there is.                             |
| Which events happened inside which trip                | **Trip + Events**              | Events nest under the trip they belong to.                             |
| Vehicle inspection records                             | **MVI**                        | Runs on its own. Cannot be combined.                                   |

Find your question in the left column.

### Three rules that save you a rerun

1.  ##### Pick the narrowest report that answers the question

    If Trip answers it, do not run Positions. Detail you do not need costs you generation time and a harder file to read.

2.  ##### Start with a short date range

    One day. Confirm the report shape is right, then widen. A month-long Positions report that comes back wrong is a month of waiting for nothing.

3.  ##### Add the companion, not another level

    Want stops? Add Stop and Idle to Trip. Do not add Positions and try to reconstruct stops from GPS pings by hand.

> **Tip:** If two reports both seem right, the one that produces fewer rows is usually the correct answer.

### Common mistakes

| Mistake                                            | What happens                          | Do this instead                         |
|----------------------------------------------------|---------------------------------------|-----------------------------------------|
| Selecting Positions for a whole fleet, for a month | Report fails or hits the record limit | One vehicle, one day, then widen        |
| Trying to add Events to Stop and Idle              | The option is disabled                | Run them as two separate reports        |
| Adding MVI to an existing selection                | Everything else is cleared            | Run MVI on its own                      |
| Selecting both Events and Event IVMS               | They occupy the same level            | Choose whichever format your team reads |

------------------------------------------------------------------------

