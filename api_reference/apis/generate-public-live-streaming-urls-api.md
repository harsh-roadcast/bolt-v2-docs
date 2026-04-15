# Generate Public Live Streaming URLs API

Generates temporary URLs for **live camera streaming** and **history playback** for a given device.

### Authentication

{% hint style="info" %}
Note: As this is a Push API, the client must verify incoming requests from the server.
{% endhint %}

All APIs require the header:

```shellscript
Authorization: Bearer <token> (Client configured)
```

### Endpoint

{% hint style="info" %}
_Configured by Client_
{% endhint %}

```shellscript
POST https://api.example-platform.com/rest/integrations/generate-public-live-streaming-urls
```

### HTTP Method

```http
POST
```

### Request Headers

| Header       | Value                                |
| ------------ | ------------------------------------ |
| Content-Type | `application/json`                   |
| X-API-KEY    | Bearer `<token>` (Client configured) |

### Sample Request

This is an example of the cURL request you will send to the endpoint:

```bash
curl --location 'https://api.example-platform.com/rest/integrations/generate-public-live-streaming-urls' \
  -H 'Content-Type: application/json' \
  -H 'X-API-KEY: <Your API_KEY Here>' \
  -d '{
    "imei": "<your device IMEI id>",
    "validityMinutes": 60
}'
```

### Request Body

```json
{
    "imei": "<your device IMEI id>",
    "validityMinutes": 60
}
```

***

### Parameters

| imei            | `String`  | Yes | The unique 15-digit International Mobile Equipment Identity number of the device.   |
| --------------- | --------- | --- | ----------------------------------------------------------------------------------- |
| validityMinutes | `Integer` | Yes | The duration (in minutes) for which the generated streaming URL will remain active. |

### Sample Response

```json
{
    "data": {
        "GeneratePublicLiveStreamingUrls": {
            "liveStreamingUrl": "https://live-streaming-v2.web.app/protocols/cvpro/index.html?t=143dfa933a9c49b6ba2f64bb182bd005&serverUrl=https://be-dev.track360.net.in/report/graphql",
            "historyPlaybackUrl": "https://live-streaming-v2.web.app/protocols/cvpro/index_timeline.html?t=143dfa933a9c49b6ba2f64bb182bd005&serverUrl=https://be-dev.track360.net.in/report/graphql",
            "validUntil": "2026-04-15T08:49:45.06798171Z"
        }
    }
}
```

{% hint style="info" %}
**Note**: Streaming URLs are time-limited and expire automatically based on the `validUntil` timestamp.
{% endhint %}

***
