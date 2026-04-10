# Device Streaming & Telemetry API Documentation

This document describes the APIs required to:

1. Generate **live video streaming URLs** for a device
2. Retrieve the **Device ID using IMEI**
3. Fetch **historical path/location data** for a device

All examples below use **sanitized domains, API keys, IMEIs, and response values** for documentation purposes.

***

### Generate Public Live Streaming URLs

Generates temporary URLs for **live camera streaming** and **history playback** for a given device.

#### Authentication

{% hint style="info" %}
Note: As this is a Push API, the client must verify incoming requests from the server.
{% endhint %}

All APIs require the header:

```
X-API-KEY: your_api_key_here
```

#### Endpoint

{% hint style="info" %}
_Configured by Client_
{% endhint %}

```
POST https://api.example-platform.com/report/graphql/GeneratePublicLiveStreamingUrls
```

#### Headers

| Header       | Value                |
| ------------ | -------------------- |
| Content-Type | `application/json`   |
| X-API-KEY    | your\_api\_key\_here |

#### Request Body

```json
{
  "query": "query GeneratePublicLiveStreamingUrls { GeneratePublicLiveStreamingUrls(imei: \"867451039284561\", validityMinutes: 60) { liveStreamingUrl historyPlaybackUrl validUntil } }",
  "variables": {},
  "operationName": "GeneratePublicLiveStreamingUrls"
}
```

#### Parameters

| Field           | Type    | Description                      |
| --------------- | ------- | -------------------------------- |
| imei            | string  | Device IMEI number               |
| validityMinutes | integer | URL validity duration in minutes |

***

#### Sample Response

```json
{
  "data": {
    "GeneratePublicLiveStreamingUrls": {
      "liveStreamingUrl": "https://streaming.example-cdn.com/player/live/index.html?t=9a3fbc2e4d6a7b1c8f0d12aaef45b890&serverUrl=https://api.example-platform.com/report/graphql",
      "historyPlaybackUrl": "https://streaming.example-cdn.com/player/history/index_timeline.html?t=9a3fbc2e4d6a7b1c8f0d12aaef45b890&serverUrl=https://api.example-platform.com/report/graphql",
      "validUntil": "2026-05-18T12:30:45.000Z"
    }
  }
}
```

***

### Get Device ID Using IMEI

Retrieves device metadata including **Device ID**, which is required for most telemetry and reporting APIs.

#### Endpoint

```
POST https://api.example-platform.com/fleet/graphql/DeviceQuery
```

#### Headers

```
X-API-KEY: your_api_key_here
Content-Type: application/json
```

#### Request Body

```json
{
  "query": "query DeviceQuery($where: DeviceWhereInput) { DeviceQuery(where: $where) { edges { node { id imei name } } } }",
  "variables": {
    "where": {
      "imei": "867451039284561"
    }
  },
  "operationName": "DeviceQuery"
}
```

***

#### Sample Response

```json
{
  "data": {
    "DeviceQuery": {
      "edges": [
        {
          "node": {
            "id": "c1b9e2a4-6f23-4c91-bb4a-0c8f1d9e6a52",
            "imei": "867451039284561",
            "name": "Vehicle-Camera-Unit-12"
          }
        }
      ]
    }
  }
}
```

***

### Fetch Device Path History

Returns **historical GPS and telemetry data** for one or more devices between a time range.

#### Endpoint

```
POST https://api.example-platform.com/graphql
```

#### Headers

```
X-API-KEY: your_api_key_here
Content-Type: application/json
```

***

#### Request Body

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

***

#### Parameters

| Field                   | Type     | Description                     |
| ----------------------- | -------- | ------------------------------- |
| deviceIds               | array    | List of device IDs              |
| fromTimestamp           | datetime | Start time of the report        |
| toTimestamp             | datetime | End time of the report          |
| positionFilterBySeconds | integer  | Sampling interval for positions |

***

#### Sample Response

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

***

### Typical Integration Flow

Clients typically follow this order when integrating:

1.  **Get Device ID**

    ```
    IMEI → DeviceQuery → Device ID
    ```
2.  **Generate Streaming URLs**

    ```
    IMEI → GeneratePublicLiveStreamingUrls → Live & Playback URLs
    ```
3.  **Fetch Telemetry / Path History**

    ```
    Device ID → ReportPosition → GPS & movement history
    ```

***

***

#### Notes

* Streaming URLs are **time-limited** and expire automatically.
* Path history queries may return **large datasets** depending on the time range.
* It is recommended to **limit time ranges or apply sampling filters** for better performance.

***
