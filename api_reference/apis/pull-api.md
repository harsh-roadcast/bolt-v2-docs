# Pull API

### Overview

This API provides real-time tracking and vehicle telematics data. It returns detailed position and\
status data for all associated devices.

### Authentication

This API uses **Basic Authentication**.

#### Example Header

```
Authorization: Basic bGl0aGl1bTpBYmNAMTIz
```

<p align="center">Replace the encoded string with your Base64-encoded <strong>username:password</strong>.</p>

### Endpoint

```
GET https://example.com/api/v1/auth/pull_api_v2?show_address=true
```

### HTTP Method

```
POST       // with empty body
```

or

```
GET
```

### Request Headers

<table><thead><tr><th width="258.9921875">Header</th><th>Value</th></tr></thead><tbody><tr><td>Content-Type</td><td> application/json </td></tr><tr><td>Authorization</td><td> Bearer <code>&#x3C;token> (Base64 encoded credentials)</code>   </td></tr></tbody></table>

### Request Parameters

<table><thead><tr><th width="180.45703125">Parameter</th><th width="171.26953125">Type</th><th>Description</th></tr></thead><tbody><tr><td>show_address</td><td>boolean</td><td>If true, includes formatted address</td></tr></tbody></table>

### Sample cURL

```
curl --location 'https://test-track.roadcast.net/api/v1/auth/pull_api_v2?
show_address=true' \
--header 'Authorization: Basic bGl0aGl1bTpBYmNAMTIz' \
--data ''
```

### Response Structure

```
{
"data": [...],
"error": [...]
}
```

### List of Device Details

<table><thead><tr><th width="213.55078125">Field</th><th width="184.58203125">Type</th><th>Description</th></tr></thead><tbody><tr><td>ac</td><td>boolean</td><td>AC status (on/off)</td></tr><tr><td>address</td><td>string</td><td>Geocoded address of the device</td></tr><tr><td>alarm</td><td>string</td><td>Alarm status (if any)</td></tr><tr><td>batteryLevel</td><td>float</td><td>Device battery level (%)</td></tr><tr><td>course</td><td>float</td><td>Direction in degrees</td></tr><tr><td>daily_distance</td><td>float</td><td>Distance traveled today (meters)</td></tr><tr><td>deviceFixTime</td><td>datetime</td><td>GPS fix timestamp</td></tr><tr><td>deviceId</td><td>string</td><td>Internal device ID</td></tr><tr><td>deviceImei</td><td>string</td><td>IMEI of the tracking device</td></tr><tr><td>deviceTime</td><td>datetime</td><td>Time recorded by device</td></tr><tr><td>external_power</td><td>any</td><td>External power supply status</td></tr><tr><td>fuel</td><td>any</td><td>Fuel level if supported</td></tr><tr><td>ignition</td><td>boolean</td><td>Ignition status</td></tr><tr><td>lastUpdate</td><td>datetime</td><td>Last update time received</td></tr><tr><td>latitude</td><td>float</td><td>Latitude coordinate</td></tr><tr><td>longitude</td><td>float</td><td>Longitude coordinate</td></tr><tr><td>name</td><td>string</td><td>Vehicle number or label</td></tr><tr><td>phone</td><td>string</td><td>Phone number linked (if any)</td></tr><tr><td>region</td><td>string</td><td>Regional tag (if any)</td></tr><tr><td>soc</td><td>string</td><td>State of charge (if applicable)</td></tr><tr><td>speed</td><td>float</td><td>Current speed (km/h)</td></tr><tr><td>status</td><td>any</td><td>Device or trip status</td></tr><tr><td>type</td><td>any</td><td>Device type</td></tr><tr><td>valid</td><td>int</td><td>1 for valid GPS fix, 0 otherwise</td></tr></tbody></table>

### Alerts

**Vehicle & Movement Alerts**

| Alert                                      | Description                                                  |
| ------------------------------------------ | ------------------------------------------------------------ |
| accident                                   | Crash detected based on impact sensor data.                  |
| movement                                   | Vehicle started moving.                                      |
| overspeed                                  | Vehicle exceeded configured speed limit.                     |
| tow                                        | Vehicle is being towed (ignition off but movement detected). |
| vibration                                  | Vibration detected while parked.                             |
| shock                                      | Strong impact detected.                                      |
| hardAcceleration                           | Sudden aggressive acceleration.                              |
| hardBraking                                | Sudden harsh braking.                                        |
| hardCornering                              | Sharp turn at high speed.                                    |
| laneChange                                 | Sudden lane change detected.                                 |
| laneDepartureAlam                          | Vehicle drifting out of lane.                                |
| dangerousDriving                           | Risky driving behavior detected.                             |
| forwardCollisionAlarm                      | Risk of front collision detected.                            |
| pedestrianCollisionAlarm                   | Risk of hitting pedestrian detected.                         |
| vehicleDistanceTooCloseToFrontVehicleAlarm | Unsafe following distance.                                   |

**Power & Battery Alerts**

| Alert                  | Description                      |
| ---------------------- | -------------------------------- |
| batteryChargingStarted | Device battery started charging. |
| batteryChargingStopped | Device battery stopped charging. |
| fullyCharged           | Battery fully charged.           |
| lowBattery             | Device battery level low.        |
| lowPower               | External power voltage is low.   |
| powerCut               | External power disconnected.     |
| powerRestored          | External power restored.         |
| powerOn                | Device powered ON.               |
| powerOff               | Device powered OFF.              |

**Security & Tampering Alerts**

| Alert               | Description                          |
| ------------------- | ------------------------------------ |
| tampering           | Device tampering detected.           |
| steelStringCut      | Tamper wire/cable cut.               |
| gpsAntennaCut       | GPS antenna disconnected or damaged. |
| jamming             | GPS/GSM signal jamming detected.     |
| removing            | Device removal attempt detected.     |
| motorLock           | Engine/motor remotely locked.        |
| motorUnlock         | Engine/motor unlocked.               |
| passwordUnlock      | Unlock using password.               |
| illegalRfid         | Unauthorized RFID used.              |
| swipeIllegalCard    | Unauthorized card swiped.            |
| swipeAuthorizedCard | Authorized card swiped.              |

#### Vehicle State Alerts

| Alert Code    | Description                            |
| ------------- | -------------------------------------- |
| door          | Door opened/closed.                    |
| seatBeltEvent | Seatbelt fastened/unfastened event.    |
| backCap       | Rear cap/cover open or close.          |
| bacCapOpen    | Rear cap opened.                       |
| geofence      | Geofence event triggered.              |
| geofenceEnter | Vehicle entered defined geofence area. |
| geofenceExit  | Vehicle exited defined geofence area.  |

**Driver Monitoring Alerts (MDVR / AI Camera Based)**

| Alert Code          | Description                              |
| ------------------- | ---------------------------------------- |
| fatigueDriving      | Driver drowsiness detected.              |
| distraction         | Driver distracted (not looking at road). |
| phoneCalling        | Driver using phone while driving.        |
| smoking             | Driver smoking detected.                 |
| driverAbnormalAlarm | Abnormal driver behavior detected.       |
| fallDown            | Driver/person fell down (AI detection).  |
| sos                 | Emergency panic button pressed.          |

**Device / Communication Alerts**

| Alert Code  | Description                                        |
| ----------- | -------------------------------------------------- |
| bleRead     | Bluetooth Low Energy device data read.             |
| rfidRead    | RFID tag read successfully.                        |
| TMDEV\_Read | External device (temperature/fuel/etc.) data read. |
| general     | General-purpose alert (custom event).              |

### List of Device Errors

<table><thead><tr><th width="214.1328125">Field</th><th width="187.703125">Type</th><th>Description</th></tr></thead><tbody><tr><td>device_id</td><td>string</td><td>ID of the device (if available)</td></tr><tr><td>expired</td><td>string</td><td>Subscription expiry date</td></tr><tr><td>imei</td><td>string</td><td>IMEI of the device</td></tr><tr><td>message</td><td>string</td><td>Error description</td></tr></tbody></table>

### Example Error Message

```
{
"device_id": null,
"expired": "",
"imei": null,
"message": "This Device is Inactive - {
'prevOdometer': '14959',
'overSpeeds': '0',
'harshBrakings': '0',
'harshAccelerations': '0',
'harshCornerings': '0',
'subscription_expiry_date': '2022-04-08',
'user_ids': [1, 2, 9040, 29793, 41729, 41741, 51627, 51629, 63178],
'daily_distance': -14959.0
}"
}
```

{% hint style="info" %}
* valid = 1 indicates the GPS data is fresh and reliable.
* Fields like fuel, external\_power, and soc might be null based on device capability.
* The API does not require any body content; authentication and URL parameters are\
  sufficient.
{% endhint %}
