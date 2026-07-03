# Device Action Log (Mobilize / Immobilize)

### Overview

The `DeviceActionLogCreate` API acts as the central command center for sending instructions to hardware devices. It is primarily used when an operator needs to mobilize or immobilize a vehicle via Over-The-Air (OTA) commands.

### Architecture & System Flow

When a mobilize or immobilize command is triggered, the following automated flow executes:

1. Request Intake (REST / GraphQL Gateway): The frontend sends a request specifying the target vehicle and the action (e.g., `engineStart` or `engineStop`). The API Gateway routes this internally to the Fleet Microservice, which verifies the user's device-specific permissions.
2. Command Dispatch: Once validated, the Fleet Microservice records the request in the main database as an action log. It then immediately triggers a background hook using Redis Pub/Sub to securely pass the command to the Ingest Gateway / Server.
3. Status Tracking & Audit Trail: The Fleet Service monitors the response from the Ingest Server.
   * If dispatched successfully, the action log status is marked as Success.
   * If unreachable or failed, it is marked as Failed, guaranteeing a permanent audit log of the network outcome.
4. Instant Dashboard Updates: Upon successful dispatch, the system proactively updates the vehicle's live state in a high-speed Redis Cache. The dashboard's Polling API reads from this cache, instantly reflecting the new "Mobilized" or "Immobilized" state on the UI without waiting for the next physical GPS ping.

{% hint style="info" %}
The Ingest Server is a specialized service responsible for maintaining direct TCP/UDP network connections with the physical GPS hardware.
{% endhint %}

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
POST https://api.example-platform.com/rest/integrations/device-action-log
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
curl --location 'https://be-dev.track360.net.in/rest/integrations/device-action-log' \
--header 'Content-Type: application/json' \
--header 'X-API-KEY: dp_world_test' \
--data '{
    "input": {
        "actionType": "Command",
        "actionDescription": "engineStop",
        "devicesID": "eaa5041d-0ae2-48a7-a060-c15ba981758e"
    }
}'
```

### Example Request Body (Payload)

Here is the JSON payload representing the **Telemetry History** request:

```json
{
    "input":{
        "actionType":"Command",
        "actionDescription":"engineStop",
        "devicesID":"eaa5041d-0ae2-48a7-a060-c15ba981758e"
}
```

### List of Request Parameters

<table><thead><tr><th>Field</th><th width="249.8125">Type</th><th>Description</th></tr></thead><tbody><tr><td>actionType</td><td>string</td><td>The category of the action being performed (e.g., <code>Command</code>).</td></tr><tr><td>actionDescription</td><td>string</td><td>The specific instruction sent to the device (e.g., <code>engineStop</code>, <code>engineStart</code>).</td></tr><tr><td>devicesID</td><td>string</td><td>The unique UUID of the target hardware device. is <a href="retrieve-device-id-by-imei-api.md">retrieved by IMEI</a></td></tr></tbody></table>

### Sample Response

Here is the expected response containing the telemetry rows:

```json
{
    "data": {
        "DeviceActionLogCreate": {
            "id": "4e6db43c-408f-4084-b055-4673a360898b",
            "deviceID": "eaa5041d-0ae2-48a7-a060-c15ba981758e",
            "actionType": "Command",
            "actionDescription": "engineStop",
            "status": "Pending",
            "createdAt": "2026-07-03T05:11:44.500061544Z",
            "updatedAt": "2026-07-03T05:11:44.500062079Z"
        }
    }
}

```

### List Of Response Parameters

| Field               | Type     | Description                                                          |
| ------------------- | -------- | -------------------------------------------------------------------- |
| `id`                | string   | The unique identifier for this specific action log entry.            |
| `deviceID`          | string   | The UUID of the device the command was sent to.                      |
| `actionType`        | string   | The category of the action logged.                                   |
| `actionDescription` | string   | The specific command executed.                                       |
| `status`            | string   | Current state of the command (e.g., `Pending`, `Success`, `Failed`). |
| `createdAt`         | datetime | UTC timestamp of when the action log was created.                    |
| `updatedAt`         | datetime | UTC timestamp of when the action log was last updated.               |

