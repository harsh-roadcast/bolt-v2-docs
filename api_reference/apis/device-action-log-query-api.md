# Device Action Log Query API

### Overview

While the Create API is used to send commands, the `DeviceActionLogQuery` API acts as the system's "Reporting and Verification" engine. It allows the frontend, administrators, or internal systems to look up the history and status of any commands previously sent to the hardware.

#### Live Status Polling

This API is critical for asynchronous command tracking:

1. After a user clicks "Mobilize", the frontend uses this Query API to check the specific action log ID.
2. If a hardware device is offline and the command gets queued (e.g., `Status: Pending`), the frontend can periodically poll this API.
3. This polling ensures the UI knows exactly when the network eventually processes the command and updates the status to `Success` or `Failed`.

### Authentication

{% hint style="info" %}
**Note**: As this is a Push API, the client must verify incoming requests from the server.
{% endhint %}

This API uses API Key authentication configured by the client.

```http
X-API-KEY: your_api_key_here
```

### Endpoint

{% hint style="info" %}
_Configured by Client_
{% endhint %}

```http
POST https://api.example-platform.com/rest/integrations/device-action-log-query
```

### HTTP Method

```http
POST
```

### Request Headers

| **Header**   | **Value**           |
| ------------ | ------------------- |
| Content-Type | `application/json`  |
| X-API-KEY    | `your_api_key_here` |

### Sample Request

This is an example of the cURL request you will send to the endpoint:

```bash
curl --location 'https://com.example.net.in/rest/integrations/device-action-log-query' \
--header 'X-API-KEY: dp_world_test' \
--header 'Content-Type: application/json' \
--data '{
    "where": {
        "id": "2ad3560e-fdd4-4f7e-9fa9-17a15fcb338b"
    }
}'
```

### Example Request Body (Payload)

Here is the JSON payload representing the **Telemetry History** request:

```json
{
    "where": {
        "id": "2ad3560e-fdd4-4f7e-9fa9-17a15fcb338b"
    }
}
```

### List of Parameters

<table><thead><tr><th>Field</th><th width="249.8125">Type</th><th>Description</th></tr></thead><tbody><tr><td>where</td><td>object</td><td>The wrapper for search filters.</td></tr><tr><td>where.id</td><td>string</td><td>The unique UUID of the action log entry you wish to query.</td></tr></tbody></table>

### Sample Response

Here is the expected response containing the telemetry rows:

```json
{
    "data": {
        "DeviceActionLogQuery": {
            "edges": [
                {
                    "node": {
                        "actionDescription": "engineStop",
                        "actionType": "Command",
                        "additionalinfo": null,
                        "createdAt": "2026-07-02T18:07:48.596904+05:30",
                        "deletedAt": null,
                        "deviceID": "eaa5041d-0ae2-48a7-a060-c15ba981758e",
                        "id": "2ad3560e-fdd4-4f7e-9fa9-17a15fcb338b",
                        "status": "Success",
                        "updatedAt": "2026-07-02T18:07:48.709832+05:30"
                    }
                }
            ],
            "pageInfo": {
                "hasNextPage": false,
                "hasPreviousPage": false,
                "startCursor": "gaFpxBAq01YO/dRPfp+pF6FfyzOL",
                "endCursor": "gaFpxBAq01YO/dRPfp+pF6FfyzOL"
            },
            "totalCount": 1
        }
    }
}
```

### List Of Response Parameters

| Field                             | Type            | Description                                                       |
| --------------------------------- | --------------- | ----------------------------------------------------------------- |
| `data.DeviceActionLogQuery.edges` | array           | A list of result wrappers, each containing a `node`.              |
| `node.id`                         | string          | The unique identifier for this specific action log entry.         |
| `node.deviceID`                   | string          | The UUID of the queried device.                                   |
| `node.actionType`                 | string          | The category of the action logged (e.g., `Command`).              |
| `node.actionDescription`          | string          | The specific command that was executed (e.g., `engineStop`).      |
| `node.status`                     | string          | Current network execution state (`Pending`, `Success`, `Failed`). |
| `node.additionalinfo`             | string / null   | Any extra error messages or context returned by the hardware.     |
| `node.createdAt`                  | datetime        | ISO timestamp of when the action log was created.                 |
| `node.updatedAt`                  | datetime        | ISO timestamp of when the action log was last updated.            |
| `node.deletedAt`                  | datetime / null | ISO timestamp if the log was soft-deleted.                        |
| `pageInfo.hasNextPage`            | boolean         | Indicates if there are more pages of results available.           |
| `pageInfo.hasPreviousPage`        | boolean         | Indicates if there is a previous page of results.                 |
| `pageInfo.startCursor`            | string          | The pagination cursor for the first item in the current set.      |
| `pageInfo.endCursor`              | string          | The pagination cursor for the last item in the current set.       |
| `totalCount`                      | integer         | Total number of records matching the query filters.               |
