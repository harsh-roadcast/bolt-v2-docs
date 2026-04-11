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
POST https://api.example-platform.com/report/graphql
```

### HTTP Method

```http
POST
```

### Request Headers

| Header        | Value                                |
| ------------- | ------------------------------------ |
| Content-Type  | `application/json`                   |
| Authorization | Bearer `<token>` (Client configured) |

### Sample Request

This is an example of the cURL request you will send to the endpoint:

```bash
curl --location 'https://bolt-revamp-dev.track360.net.in/graphql' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_JWT_TOKEN_HERE>' \
  -d '{
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

***

### Parameters

| Field           | Type    | Description                      |
| --------------- | ------- | -------------------------------- |
| imei            | string  | Device IMEI number               |
| validityMinutes | integer | URL validity duration in minutes |

### Sample Response

```json
{
  "data": {
    "GeneratePublicLiveStreamingUrls": {
      "liveStreamingUrl": "https://bolt-test.web.app/assets/protocols/cvpro/index.html?t=22a41b6693b74129a27569564b38e319&serverUrl=https://be-dev.track360.net.in/report/graphql",
      "historyPlaybackUrl": "https://bolt-test.web.app/assets/protocols/cvpro/index_timeline.html?t=22a41b6693b74129a27569564b38e319&serverUrl=https://be-dev.track360.net.in/report/graphql",
      "validUntil": "2026-04-11T08:21:21.600627735Z"
    }
  }
}
```

{% hint style="info" %}
**Note**: Streaming URLs are time-limited and expire automatically based on the `validUntil` timestamp.
{% endhint %}

***
