# Position Pull API (V2)

### Overview

This API provides the latest real-time tracking, telemetry, and position data for all associated devices.

### Authentication

This API uses API Key authentication via a custom HTTP header.

#### Example Header

```bash
X-API-KEY: API_KEY_HERE
```

_Replace_ `API_KEY_HERE` _with your valid API key._

### Endpoint

```bash
GET https://client-domain.com/api/v2/rest/integrations/pull-positions-api
```

### HTTP Method

```
POST 
```

### Request Headers

<table><thead><tr><th width="258.9921875">Header</th><th>Value</th></tr></thead><tbody><tr><td>Content-Type</td><td> application/json </td></tr><tr><td>X-API-KEY</td><td><code>&#x3C;your_api_key></code></td></tr></tbody></table>

### Request Parameters

<table><thead><tr><th width="180.45703125">Parameter</th><th width="171.26953125">Type</th><th>Description</th></tr></thead><tbody><tr><td>input</td><td>object</td><td>An empty JSON object <code>{}</code> triggering the retrieval of all current device positions under your organisation.</td></tr></tbody></table>

### Input Parameters

In the input parameter of request these optional parameter can be passed to filter the incoming positions on the provided basis.

| Parameter   | Type               | Description                                 |
| ----------- | ------------------ | ------------------------------------------- |
| deviceIds   | `uuid`(Optional)   | Filter devices on the basis if device IDs   |
| deviceImeis | `String`(Optional) | Filter devices on the basis of IMEIs        |
| deviceNames | `String`(Optional) | Filter devices on the basis on device names |

### Sample cURL

```bash
curl --location 'https://example.net/api/v2/rest/integrations/pull-positions-api \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: dp_world_test" \
  -d '{"input":{}}'
```

### Response Structure

```json
{
  "data": [
    // Array of device position objects (latitude, longitude, speed etc.)
  ],
  "error": null
}
```

{% hint style="info" %}
* valid = 1 indicates the GPS data is fresh and reliable.
* The API does not require any body content; authentication and URL parameters are\
  sufficient.
{% endhint %}
