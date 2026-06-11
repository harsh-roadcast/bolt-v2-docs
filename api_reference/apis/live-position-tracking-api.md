# Live Position Tracking API

### Overview

Retrieves live position tracking data for devices. This API allows the client to fetch recent device locations while defining custom thresholds for determining if a device is currently "idle" or "inactive".

### Authentication

This API uses API Key authentication configured by the client.

```http
X-API-KEY: your_api_key_here
```

### Endpoint

{% hint style="info" %}
_Configured by Client_
{% endhint %}

```http
POST https://api.example-platform.com/rest/integrations/live-position-tracking
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
curl --location 'https://api.example-platform.com/rest/integrations/live-position-tracking' \
--header 'Content-Type: application/json' \
--header 'X-API-KEY: your_api_key_here' \
--data '{
    "onlyLastUpdateGte": "2026-04-13T00:00:00Z",
    "considerIdleAfterSeconds": 600,
    "considerInactiveAfterSeconds": 1800
}'
```

### Example Request Body (Payload)

Here is the JSON payload representing the **Live Position Tracking** request:

```json
{
    "onlyLastUpdateGte": "2026-04-13T00:00:00Z",
    "considerIdleAfterSeconds": 600,
    "considerInactiveAfterSeconds": 1800
}
```

### List of Parameters

| **Field Name**               | **DataType** | **Description**                                                                                                           |
| ---------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------- |
| onlyLastUpdateGte            | string       | Unique IMEI identifier of the device you are querying.                                                                    |
| considerIdleAfterSeconds     | integer      | The threshold duration in seconds after which a device is classified as "idle" if it has not moved.                       |
| considerInactiveAfterSeconds | integer      | The threshold duration in seconds after which a device is classified as "inactive" if no communication has been received. |

### Sample Response

Here is the expected response containing the internal Device ID:

```json
{
    "success": true,
    "data": [
        {
            "deviceId": "0199ec89-36ec-7c36-b291-98da56704e25",
            "status": "idle",
            "lastUpdate": "2026-04-13T00:15:30Z",
            "location": {
                "latitude": 28.7041,
                "longitude": 77.1025
            }
        }
    ]
}
```

***

