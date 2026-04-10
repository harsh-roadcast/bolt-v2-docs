# Generate Public Live Streaming API

Generates temporary URLs for **live camera streaming** and **history playback** for a given device.

### Authentication

{% hint style="info" %}
Note: As this is a Push API, the client must verify incoming requests from the server.
{% endhint %}

All APIs require the header:

```
X-API-KEY: your_api_key_here
```

### Endpoint

{% hint style="info" %}
_Configured by Client_
{% endhint %}

```
POST https://api.example-platform.com/report/graphql/GeneratePublicLiveStreamingUrls
```

### HTTP Method

```http
POST
```

### Request Headers

| Header       | Value                |
| ------------ | -------------------- |
| Content-Type | `application/json`   |
| X-API-KEY    | your\_api\_key\_here |

### Sample Request

This is an example of the cURL request you will send to the endpoint:

```bash
curl --location 'https://api.example-platform.com/report/graphql/GeneratePublicLiveStreamingUrls' \
--header 'Content-Type: application/json' \
--header 'X-API-KEY: your_api_key_here' \
--data '{
  "query": "query GeneratePublicLiveStreamingUrls { GeneratePublicLiveStreamingUrls(imei: \"867451039284561\", validityMinutes: 60) { liveStreamingUrl historyPlaybackUrl validUntil } }",
  "variables": {},
  "operationName": "GeneratePublicLiveStreamingUrls"
}'
```

### Request Body

```json
{
  "query": "query GeneratePublicLiveStreamingUrls { GeneratePublicLiveStreamingUrls(imei: \"867451039284561\", validityMinutes: 60) { liveStreamingUrl historyPlaybackUrl validUntil } }",
  "variables": {},
  "operationName": "GeneratePublicLiveStreamingUrls"
}
```

### Parameters

| Field           | Type    | Description                      |
| --------------- | ------- | -------------------------------- |
| imei            | string  | Device IMEI number               |
| validityMinutes | integer | URL validity duration in minutes |

***

### Sample Response

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

{% hint style="info" %}
**Note**: Streaming URLs are time-limited and expire automatically based on the `validUntil` timestamp.
{% endhint %}

***
