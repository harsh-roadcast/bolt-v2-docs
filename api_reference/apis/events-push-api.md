# Events Push API

### Overview

The Events Push API delivers real-time event notifications to client systems.

{% hint style="info" %}
The platform sends HTTP POST requests to a client-configured endpoint whenever a supported event occurs.
{% endhint %}

This API supports real-time updates for events such as:

* Overspeed
* Fuel Fill / Fuel Drain
* Geofence Entry / Exit
* Tampering
* Power Cut
* SOS
* etc.

***

### Endpoint

The endpoint URL is provided by the client.

Example:

```
POST https://client-domain.com/api/events
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
  "Event": "overspeed",
  "Changes": 50,
  "Device_Time": "2024-06-28T17:52:13.000000+0000",
  "IMEI": "350612075195931",
  "Server_Time": "2024-06-28T18:49:45.000000+0000",
  "Coordinates": "22.927968,75.533275",
  "Location": "Indore - Depalpur - Ingoriya Road, Kharsora, Birgoda, Depalpur Tahsil, Indore District, Madhya Pradesh, 453220, India",
  "Geofence_Name": null
}
```

***

### Payload Field Definitions

| Field          | Type          | Description                                                         |
| -------------- | ------------- | ------------------------------------------------------------------- |
| Event          | String        | Type of event (e.g., overspeed, fuel\_fill, geofence)               |
| Changes        | Integer       | Event-specific value (e.g., fuel change in liters, overspeed delta) |
| Device\_Time   | String        | Timestamp when event occurred on device (ISO 8601 with timezone)    |
| IMEI           | String        | IMEI number of the reporting device                                 |
| Server\_Time   | String        | Timestamp when event was received by server                         |
| Coordinates    | String        | Latitude,Longitude format                                           |
| Location       | String        | Human-readable address                                              |
| Geofence\_Name | String / Null | Geofence name if applicable                                         |

***

### Timestamp Format

```
YYYY-MM-DDTHH:MM:SS.SSSSSS+0000
```

Example:

```
2024-06-28T17:52:13.000000+0000
```

All timestamps are in UTC.

***

### Example HTTP Request

```http
POST /client-endpoint-url HTTP/1.1
Host: client-host
Content-Type: application/json
Authorization: Bearer <token>

{
  "Event": "overspeed",
  "Changes": 50,
  "Device_Time": "2024-06-28T17:52:13.000000+0000",
  "IMEI": "350612075195931",
  "Server_Time": "2024-06-28T18:49:45.000000+0000",
  "Coordinates": "22.927968,75.533275",
  "Location": "Indore - Depalpur - Ingoriya Road, Kharsora, Birgoda, Depalpur Tahsil, Indore District, Madhya Pradesh, 453220, India",
  "Geofence_Name": null
}
```

***

### Client Response Requirements

The client must acknowledge receipt of the event with an HTTP 200 response.

#### Success Response

**Status Code:** 200 OK

```json
{
  "status": "success",
  "message": "Event received successfully."
}
```

***

#### Error Response

**Status Code:** 4xx or 5xx

```json
{
  "status": "error",
  "message": "Detailed error message here."
}
```

***

### Retry Policy (Recommended)

If the client endpoint does not return HTTP 200:

* The server may retry delivery
* Recommended: exponential backoff retry mechanism
* Ensure idempotency at client side to avoid duplicate processing

***

### Security Best Practices

* Use HTTPS (TLS 1.2+)\\
* Validate Bearer token (if enabled)\\
* Whitelist server IPs\\
* Implement request signature verification (optional enterprise enhancement)

***

### Validation Rules

* Coordinates must be in latitude,longitude format\\
* IMEI must be numeric and 15 digits\\
* Device\_Time ≤ Server\_Time\\
* Event field cannot be empty

***

### Supported Event Types (Indicative)

Event Description

***

overspeed Speed threshold exceeded fuel\_fill Fuel filling detected fuel\_drain Fuel theft detected geofence\_enter Entered geofence geofence\_exit Exited geofence tampering Device tampering power\_cut External power disconnected sos Emergency alert

***

### Integration Notes

* Client endpoint must be capable of handling concurrent POST requests
* Recommended response time < 2 seconds
* Ensure endpoint availability (99.9%+ uptime for enterprise integrations)

***
