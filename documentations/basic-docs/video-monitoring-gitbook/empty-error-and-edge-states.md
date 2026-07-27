## 22. Empty, Error and Edge States

| Scenario | Expected behavior |
|---|---|
| No streams available | Show empty state with explanation and no broken grid. |
| Filters return no streams | Show `No videos match your filters` with clear filters action. |
| Stream connection fails | Show card-level error and retry. |
| Many streams fail | Show page-level warning and Retry action. |
| Stream reconnects | Keep card position and update status. |
| Device offline | Show offline state and avoid endless retries. |
| User lacks permission | Hide restricted video content and show permission message if user navigates directly. |
| Evidence clip unavailable | Keep metadata visible and show clip unavailable state. |
| No incidents | Show PAP empty state and zero metrics. |
| Invalid history input | Ask user to select required time values. |
| No historical video found | Show no data state without clearing selected inputs. |
| Download fails | Show failure and allow retry. |
| Call fails | Show connection error and allow reconnect/disconnect. |

---
