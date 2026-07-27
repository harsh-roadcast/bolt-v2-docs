## 18. AI Insights

AI Insights translates health signals into short, prioritized operational observations.

### 18.1 Approved insight pattern

Each insight contains:

- A concise issue title.
- Supporting evidence or context.
- An affected-device count where available.
- A `View devices` action.

Examples represented in the approved state include:

- Devices not reporting.
- Current power issues.
- Persistent poor GPS.

### 18.2 Insight rules

- Insights must be based on current organisation data.
- Every numeric claim must be traceable to the underlying device set.
- Similar device-level issues should be grouped.
- Duplicate insights must be suppressed.
- Urgent connectivity or power failures should rank above low-risk observations.
- An insight must add explanation or action, not merely repeat a chart label.

### 18.3 Navigation

`View devices` should:

- Apply the relevant Problem Vehicles filter when the destination remains on Home, or
- Open the relevant device list with the issue filter preserved.

The destination must retain organisation scope and permissions.

### 18.4 AI safety and fallback

- Generated wording must not change the underlying counts.
- If narrative generation is unavailable, rule-based insight copy should be shown.
- Home must never invent a diagnosis unsupported by telemetry.
- Low-confidence conclusions should be identified as such.
- No-insight state should read as a normal healthy state, not an error.

---
