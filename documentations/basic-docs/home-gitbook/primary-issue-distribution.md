## 17. Primary Issue Distribution

Primary Issue Distribution shows how devices needing attention are grouped by their highest-priority active issue.

### 17.1 Approved issue categories

- Not Reporting.
- Power Issue.
- Invalid GPS.
- Delayed Packet.
- Poor GPS.
- Poor Network.

### 17.2 Primary-issue rule

The approved copy states that each affected device is counted once under its highest-priority issue.

This requires:

- A single shared priority order in the backend.
- One primary issue per device for this chart.
- Secondary issues to remain available in the Problem Vehicles table.
- The chart total to equal the number of distinct affected devices represented.

### 17.3 Chart behavior

- Each category uses a stable color.
- The legend shows the category and count.
- Colors remain consistent wherever the same issue is used on Home.
- Hover or keyboard focus should reveal category and count.
- Selecting a segment or legend item may apply the corresponding Problem Vehicles filter.
- A filter interaction must be visually clear and reversible.

### 17.4 Empty state

When there are no active issues:

- Do not show an empty donut without explanation.
- Show a healthy confirmation state.
- Keep the information control available.
- Do not create artificial zero-value legend noise.

---
