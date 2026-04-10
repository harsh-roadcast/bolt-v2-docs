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
POST https://api.example-platform.com/graphql
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
curl --location 'https://api.example-platform.com/graphql' \
--header 'Content-Type: application/json' \
--header 'X-API-KEY: your_api_key_here' \
--data '{
  "query": "query ReportPosition($input: ReportQueryInput!) { ReportPosition(input: $input) { rows { deviceId speed temperature ignition distance motion latitude longitude gpsFixTimestamp deviceTimestamp serverTimestamp } extras } }",
  "variables": {
    "input": {
      "splitIntoDailyIntervals": false,
      "withAddress": false,
      "positionIgnoreFilterOutline": false,
      "positionFilterSpeedGreaterThan": 0,
      "positionFilterSpeedLesserThan": 0,
      "positionFilterBySeconds": 60,
      "fetchByDeviceTime": false,
      "deviceIds": [
        "c1b9e2a4-6f23-4c91-bb4a-0c8f1d9e6a52"
      ],
      "fromTimestamp": "2026-05-18T00:00:00.000Z",
      "toTimestamp": "2026-05-18T04:00:00.000Z"
    }
  },
  "operationName": "ReportPosition"
}'
```

### Example Request Body (Payload)

Here is the JSON payload representing the GraphQL request:

```json
{
  "query": "query ReportPosition($input: ReportQueryInput!) { ReportPosition(input: $input) { rows { deviceId speed temperature ignition distance motion latitude longitude gpsFixTimestamp deviceTimestamp serverTimestamp } extras } }",
  "variables": {
    "input": {
      "splitIntoDailyIntervals": false,
      "withAddress": false,
      "positionIgnoreFilterOutline": false,
      "positionFilterSpeedGreaterThan": 0,
      "positionFilterSpeedLesserThan": 0,
      "positionFilterBySeconds": 60,
      "fetchByDeviceTime": false,
      "deviceIds": [
        "c1b9e2a4-6f23-4c91-bb4a-0c8f1d9e6a52"
      ],
      "fromTimestamp": "2026-05-18T00:00:00.000Z",
      "toTimestamp": "2026-05-18T04:00:00.000Z"
    }
  },
  "operationName": "ReportPosition"
}
```

### List of Parameters

| **Field Name**          | **DataType** | **Description**                                         |
| ----------------------- | ------------ | ------------------------------------------------------- |
| deviceIds               | array        | List of internal device IDs (obtained via DeviceQuery). |
| fromTimestamp           | datetime     | Start time of the report (ISO 8601 format).             |
| toTimestamp             | datetime     | End time of the report (ISO 8601 format).               |
| positionFilterBySeconds | integer      | Sampling interval for positions to reduce payload size. |

### Sample Response

Here is the expected response containing the telemetry rows:

```json
{
  "data": {
    "ReportPosition": {
      "rows": [
        {
          "deviceId": "c1b9e2a4-6f23-4c91-bb4a-0c8f1d9e6a52",
          "speed": 42,
          "temperature": 24,
          "ignition": true,
          "distance": 1.2,
          "motion": true,
          "latitude": 28.613912,
          "longitude": 77.209021,
          "gpsFixTimestamp": "2026-05-18T00:01:10Z",
          "deviceTimestamp": "2026-05-18T00:01:10Z",
          "serverTimestamp": "2026-05-18T00:01:12.480Z"
        },
        {
          "deviceId": "c1b9e2a4-6f23-4c91-bb4a-0c8f1d9e6a52",
          "speed": 38,
          "temperature": 25,
          "ignition": true,
          "distance": 2.1,
          "motion": true,
          "latitude": 28.614201,
          "longitude": 77.210442,
          "gpsFixTimestamp": "2026-05-18T00:02:10Z",
          "deviceTimestamp": "2026-05-18T00:02:10Z",
          "serverTimestamp": "2026-05-18T00:02:11.193Z"
        }
      ],
      "extras": {}
    }
  }
}
```

{% hint style="info" %}
**Note**: Path history queries may return large datasets. Use `positionFilterBySeconds` or limit the timestamp range for better performance.
{% endhint %}
