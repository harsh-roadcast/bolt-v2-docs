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

### Authentication

This API uses **Basic Authentication**.

#### Example Header

```bash
Authorization: Basic abcd123efgh4567890
```

<p align="center">Replace the encoded string with your Base64-encoded <strong>username:password</strong>.</p>

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

* Use HTTPS (TLS 1.2+)
* Validate Bearer token (if enabled)
* Whitelist server IPs
* Implement request signature verification (optional enterprise enhancement)

***

### Validation Rules

* Coordinates must be in latitude,longitude format
* IMEI must be numeric and 15 digits
* Device\_Time ≤ Server\_Time
* Event field cannot be empty

***

### Supported Event Types (Indicative)  &#x20;

| Label                           | Short Description                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------- |
| stoppage                        | The vehicle has come to a complete stop for a specific duration.                   |
| geofenceExit                    | The device has exited a pre-defined geographical boundary.                         |
| geofenceEnter                   | The device has entered a pre-defined geographical boundary.                        |
| geofenceSpeedLimitExceed        | The vehicle exceeded the specific speed limit assigned to a geofence.              |
| engineResume                    | The engine has resumed operation after a stop or cut-off.                          |
| engineStop                      | The engine has been turned off or remotely immobilized.                            |
| ignitionOn                      | The vehicle ignition has been turned on (key in).                                  |
| ignitionOff                     | The vehicle ignition has been turned off.                                          |
| over\_ignition                  | The ignition has been on for an excessive period without movement.                 |
| ac\_idle                        | The air conditioning is running while the vehicle is stationary (idling).          |
| idle                            | The engine is running, but the vehicle is not moving.                              |
| night\_driving / nightDriving   | The vehicle is being operated during restricted night hours.                       |
| deviceOverspeed                 | The vehicle has exceeded the configured global speed limit.                        |
| over\_motion                    | Excessive motion or vibration detected (often while parked or towed).              |
| RouteDeviation / routeDeviation | The vehicle has strayed from its assigned or scheduled path.                       |
| delayed\_trip\_start            | The trip did not begin by the scheduled start time.                                |
| delay\_in\_trip\_end            | The trip was not completed by the scheduled end time.                              |
| etaStartTrip                    | Estimated Time of Arrival calculation for the start of a trip.                     |
| etaEndTrip                      | Estimated Time of Arrival calculation for the end of a trip.                       |
| etaDelayedTripEnd               | The estimated arrival time suggests the trip will finish later than scheduled.     |
| etaHaltPointReach               | The vehicle has reached a scheduled intermediate stop (halt point).                |
| etaHaltPointExit                | The vehicle has left a scheduled intermediate stop.                                |
| network\_disconnect             | The device has lost connection to the cellular network.                            |
| gps\_disconnect                 | The device has lost the GPS satellite signal (no location fix).                    |
| imeiChanged                     | The SIM card or device hardware (IMEI) associated with the asset has changed.      |
| driverChanged                   | A new driver has been identified (e.g., via RFID or iButton).                      |
| commandResult                   | The response or acknowledgement of a remote command sent to the device.            |
| temperature                     | A periodic reading or alert regarding the device or cargo temperature.             |
| documentExpiry                  | An alert that a vehicle or driver document (e.g., license, insurance) is expiring. |

***

### Integration Notes

* Client endpoint must be capable of handling concurrent POST requests
* Recommended response time < 2 seconds
* Ensure endpoint availability (99.9%+ uptime for enterprise integrations)

***
