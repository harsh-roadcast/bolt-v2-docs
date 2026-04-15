# Fetch Device Path & Telemetry History API

### Overview

Returns historical GPS and telemetry data for one or more devices between a specific time range.

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
POST https://api.example-platform.com/rest/integrations/position-report
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
curl --location 'https://api.example-platform.com/rest/integrations/position-report' \
--header 'Content-Type: application/json' \
--header 'X-API-KEY: your_api_key_here' \
--data '{
    "input": {
        "deviceIds": ["8f8baae3-872a-4fab-8396-cf7fc17c83f7"],
        "fromTimestamp": "2026-04-10T00:00:00Z",
        "toTimestamp": "2026-04-10T04:59:59Z",
        "splitIntoDailyIntervals": false,
        "withAddress": false,
        "eventTypeFilter": null,
        "positionIgnoreFilterOutline": false,
        "positionFilterSpeedGreaterThan": 0,
        "positionFilterSpeedLesserThan": 0,
        "positionFilterBySeconds": 20,
        "fetchByDeviceTime": false
    }
}'
```

### Example Request Body (Payload)

Here is the JSON payload representing the GraphQL request:

```json
{
    "input": {
        "deviceIds": ["8f8baae3-872a-4fab-8396-cf7fc17c83f7"],
        "fromTimestamp": "2026-04-10T00:00:00Z",
        "toTimestamp": "2026-04-10T04:59:59Z",
        "splitIntoDailyIntervals": false,
        "withAddress": false,
        "eventTypeFilter": null,
        "positionIgnoreFilterOutline": false,
        "positionFilterSpeedGreaterThan": 0,
        "positionFilterSpeedLesserThan": 0,
        "positionFilterBySeconds": 20,
        "fetchByDeviceTime": false    
    }
}
```

### List of Parameters

<table data-header-hidden><thead><tr><th width="263.5390625">Parameter</th><th width="140.26171875">Type</th><th width="108.31640625">Required</th><th>Description</th></tr></thead><tbody><tr><td>deviceIds</td><td><code>Array&#x3C;String></code></td><td>Yes</td><td>A list of UUIDs representing the tracking devices.</td></tr><tr><td>fromTimestamp</td><td><code>ISO 8601</code></td><td>Yes</td><td>The start date/time for the report (UTC).</td></tr><tr><td>toTimestamp</td><td><code>ISO 8601</code></td><td>Yes</td><td>The end date/time for the report (UTC).</td></tr><tr><td>splitIntoDailyIntervals</td><td><code>Boolean</code></td><td>No</td><td>If <code>true</code>, results are grouped by day.</td></tr><tr><td>withAddress</td><td><code>Boolean</code></td><td>No</td><td>If <code>true</code>, the API performs reverse geocoding to include street addresses.</td></tr><tr><td>eventTypeFilter</td><td><code>String/Null</code></td><td>No</td><td>Filter by specific event types (e.g., "Ignition On"). Use <code>null</code> for all.</td></tr><tr><td>positionIgnoreFilterOutline</td><td><code>Boolean</code></td><td>No</td><td>If <code>true</code>, ignores the predefined geofence or boundary filters.</td></tr><tr><td>positionFilterSpeedGreaterThan</td><td><code>Integer</code></td><td>No</td><td>Minimum speed threshold (km/h) for positions to be included.</td></tr><tr><td>positionFilterSpeedLesserThan</td><td><code>Integer</code></td><td>No</td><td>Maximum speed threshold (km/h) for positions to be included.</td></tr><tr><td>positionFilterBySeconds</td><td><code>Integer</code></td><td>No</td><td>Throttles data points (e.g., 20 means "return one point every 20 seconds").</td></tr><tr><td>fetchByDeviceTime</td><td><code>Boolean</code></td><td>No</td><td>If <code>true</code>, uses the timestamp recorded by the hardware rather than the server receipt time.</td></tr></tbody></table>

### Sample Response

Here is the expected response containing the telemetry rows:

```json
{
"data": {
        "ReportPosition": {
            "extras": {},
            "rows": [
                {
                    "deviceId": "8f8baae3-872a-4fab-8396-cf7fc17c83f7",
                    "speed": 72,
                    "temperature": 0,
                    "ignition": true,
                    "distance": 0,
                    "motion": true,
                    "latitude": 26.328853,
                    "longitude": 72.890081,
                    "gpsFixTimestamp": "2026-04-10T00:00:07Z",
                    "deviceTimestamp": "2026-04-10T00:00:07Z",
                    "serverTimestamp": "2026-04-10T00:00:07.93Z"
                },
                {
                    "deviceId": "8f8baae3-872a-4fab-8396-cf7fc17c83f7",
                    "speed": 67,
                    "temperature": 0,
                    "ignition": true,
                    "distance": 0.37624318722387035,
                    "motion": true,
                    "latitude": 26.331816999999997,
                    "longitude": 72.891902,
                    "gpsFixTimestamp": "2026-04-10T00:00:27Z",
                    "deviceTimestamp": "2026-04-10T00:00:27Z",
                    "serverTimestamp": "2026-04-10T00:00:27.913Z"
                }
            }
        }
    }
}
```

{% hint style="info" %}
**Note**: Path history queries may return large datasets. Use `positionFilterBySeconds` or limit the timestamp range for better performance.
{% endhint %}
