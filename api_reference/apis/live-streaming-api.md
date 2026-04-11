# Live Streaming API

Retrieves live streaming details, including server time, expiration, available channels, and the device unique ID, using a provided session token.

#### Authentication

{% hint style="info" %}
<p align="center"><strong>Info</strong>: For this specific endpoint, authentication is handled via a <code>token</code> argument passed directly inside the GraphQL query, rather than an HTTP header.</p>
{% endhint %}

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

| Header       | Value              |
| ------------ | ------------------ |
| Content-Type | `application/json` |

### Sample Request

This is an example of the cURL request you will send to the endpoint:

```bash
curl --location 'https://api.example-platform.com/report/graphql' \
-H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
  "query": "query LiveStreamingDetails {\n  LiveStreamingDetails(token: \"22a41b6693b74129a27569564b38e319\") {\n    serverTime\n    validUntil\n    channels\n    uniqueId\n  }\n}",
  "variables": {},
  "operationName": "LiveStreamingDetails"
}'
```

### Request Body

```json
{
  "query": "query LiveStreamingDetails {\n  LiveStreamingDetails(token: \"22a41b6693b74129a27569564b38e319\") {\n    serverTime\n    validUntil\n    channels\n    uniqueId\n  }\n}",
  "variables": {},
  "operationName": "LiveStreamingDetails"
}
```

### Parameters

| Parameter       | Type   | Required | Description                                                                                                                                  |
| --------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`         | String | Yes      | The actual GraphQL query string requesting the data.                                                                                         |
| `operationName` | String | No       | The name of the specific operation being executed (`"LiveStreamingDetails"`).                                                                |
| `variables`     | Object | No       | A JSON object containing dynamic variables. _(Note: In your curl, this is empty `{}` because the token is hardcoded into the query string)._ |

***

### Sample Response

```json
{
    "data": {
        "LiveStreamingDetails": {
            "serverTime": "2026-04-11T08:12:00.98480483Z",
            "validUntil": "2026-04-11T08:21:21.599619Z",
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
