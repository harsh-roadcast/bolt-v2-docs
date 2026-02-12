# Position Push API

### Overview

Defines the processed tracking payload structure sent from server to client systems.

{% hint style="info" %}
The platform sends HTTP POST requests to a client-configured endpoint whenever a supported event occurs.
{% endhint %}

***

### Endpoint

The endpoint URL is provided by the client.

Example:

```
POST https://client-domain.com/api/pos
```

***

### HTTP Method

```
POST
```

***

### Request Headers

&#x20;Value

<table><thead><tr><th width="220">Header</th><th width="521">Value</th></tr></thead><tbody><tr><td>Content-Type</td><td> application/json </td></tr><tr><td>Authorization</td><td> Bearer <code>&#x3C;token></code>{=html} (Optional, if enabled)</td></tr></tbody></table>

***

### Sample Payload

```json
{
  "LogsDeviceID": 12345,
  "LogsImeiNo": "867530912345678",
  "device_id": "235235235",
  "name": "Test Vehicle",
  "serverTime": "2026-01-29T10:30:00Z",
  "latitude": 28.6139,
  "longitude": 77.2090,
  "speed": 42.5,
  "course": 180,
  "totalDistance": 12345.67,
  "ignition": "ON",
  "alarm": "sos",
  "attributes": {
    "battery": 12.6,
    "satellites": 9
  }
}
```

***

### Field Definitions

#### Device Identification

| Field        | Type    | Description                 |
| ------------ | ------- | --------------------------- |
| LogsDeviceID | Integer | Internal logging ID         |
| LogsImeiNo   | String  | Device IMEI                 |
| device\_id   | String  | Application-level ID        |
| name         | String  | Device/vehicle display name |

***

#### Location & Movement

| Field         | Type    | Description          |
| ------------- | ------- | -------------------- |
| latitude      | Float   | WGS‑84 Latitude      |
| longitude     | Float   | WGS‑84 Longitude     |
| speed         | Float   | km/h                 |
| course        | Integer | 0–360 degrees        |
| totalDistance | Float   | Kilometers travelled |

***

#### Status

| Field    | Type          | Description                   |
| -------- | ------------- | ----------------------------- |
| ignition | String        | ON / OFF                      |
| alarm    | String / Null | sos, overspeed, geofence etc. |

***

#### Attributes Object

| Field      | Type    | Description          |
| ---------- | ------- | -------------------- |
| battery    | Float   | Voltage              |
| satellites | Integer | GPS satellites count |

Fields may vary depending on device configuration.
