# Consume Position API

### Overview

The Consume Position API receives position data for one or multiple devices.

***

### Endpoint

```
POST https://test.example.com/api/v1/auth/consume_api_v2
```

### Request Headers

|                  |                  |
| ---------------- | ---------------- |
| **Content-Type** | application/json |
| **Protocol**     | HTTPS (TLS 1.2+) |

***

### Request Schema

```json
{
  "position": [
    {
      "valid": "1",
      "timestamp": "1685328070",
      "lat": "28.535517",
      "lon": "77.391029",
      "speed": "42",
      "heading": "234",
      "altitude": "232",
      "batt": "100",
      "deviceUniqueId": "123456789012345",
      "vehicleNo": "DL01AB1234"
    }
  ]
}
```

***

### Field Definitions

| Field          | Type   | Mandatory | Description              |
| -------------- | ------ | --------- | ------------------------ |
| valid          | String | Yes       | "1" valid, "0" invalid   |
| timestamp      | String | Yes       | Unix epoch (seconds)     |
| lat            | String | Yes       | Latitude                 |
| lon            | String | Yes       | Longitude                |
| speed          | String | Yes       | Speed (km/h)             |
| heading        | String | Yes       | Direction (0–360)        |
| altitude       | String | No        | Altitude (meters)        |
| batt           | String | No        | Battery (%)              |
| deviceUniqueId | String | Yes       | Unique device identifier |
| vehicleNo      | String | No        | Vehicle number           |

***

### Response

#### Success

HTTP 200 OK

#### Errors

* 400 – Bad Request
* 401 – Unauthorized
* 422 – Validation Error
* 500 – Internal Server Error

***

### Validation Rules

* Latitude: -90 to +90
* Longitude: -180 to +180
* Heading: 0–360
* Speed ≥ 0
* Timestamp not future-dated beyond 5 minutes
