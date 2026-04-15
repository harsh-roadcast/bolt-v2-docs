# Live Streaming API

Retrieves live streaming details, including server time, expiration, available channels, and the device unique ID, using a provided session token.

#### Authentication

{% hint style="info" %}
**Note**: As this is a Push API, the client must verify incoming requests from the server.
{% endhint %}

This API uses API Key authentication configured by the client.

```http
X-API-KEY: your_api_key_here
```

### Endpoint

{% hint style="info" %}
_Configured by Client_
{% endhint %}

```shellscript
POST https://api.example-platform.com/rest/integrations/live-streaming-details
```

### HTTP Method

```http
POST
```

### Request Headers

| Header       | Value                |
| ------------ | -------------------- |
| Content-Type | `application/json`   |
| X-API-KEY    | \<your api key here> |

### Sample Request

This is an example of the cURL request you will send to the endpoint:

```bash
curl --location 'https://api.example-platform.com/rest/integrations/live-streaming-details' \
-H 'Content-Type: application/json' \
-H 'X-API-KEY: API_KEY' \
  -d '{
    "token": "<token>"
}'
```

### Request Body

```json
{
    "token": "<token>"
}
```

### Parameters

| Parameter | Type            | Required | Description                                                    |
| --------- | --------------- | -------- | -------------------------------------------------------------- |
| token     | `String` (UUID) | Yes      | The unique session token generated for a specific live stream. |

***

### Sample Response

```json
{
  "data": {
    "LiveStreamingDetails": {
      "serverTime": "2026-04-15T09:20:58.884362293Z",
      "validUntil": "2026-04-16T04:09:18.373Z",
      "channels": [
        1,
        2
      ],
      "uniqueId": "522076851100"
    }
  }
}
```

{% hint style="info" %}
**Note**: Streaming URLs are time-limited and expire automatically based on the `validUntil` timestamp.
{% endhint %}

***
