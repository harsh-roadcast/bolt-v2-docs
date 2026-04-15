# Retrieve Device ID by IMEI API

### Overview

Retrieves device metadata including Device ID, which is a required parameter for most telemetry and reporting APIs.

### Authentication

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

```http
POST https://api.example-platform.com/rest/integrations/device-query
```

### HTTP Method

```http
POST
```

### Request Headers

| **Header**   | **Value**           |
| ------------ | ------------------- |
| Content-Type | `application/json`  |
| X-API-KEY    | `your_api_key_here` |

### Sample Request

This is an example of the cURL request you will send to the endpoint:

```bash
curl --location 'https://api.example-platform.com/fleet/graphql/DeviceQuery' \
--header 'Content-Type: application/json' \
--header 'X-API-KEY: your_api_key_here' \
--data '{
    "where": {
        "imei": "<Your device IMEI>"
    }
}'
```

### Example Request Body (Payload)

Here is the JSON payload representing the GraphQL request:

```json
{
    "where": {
        "imei": "<Your device IMEI>"
    }
}
```

### List of Parameters

| **Field Name** | **DataType** | **Description**                                        |
| -------------- | ------------ | ------------------------------------------------------ |
| imei           | string       | Unique IMEI identifier of the device you are querying. |

### Sample Response

Here is the expected response containing the internal Device ID:

```json
{
    "data": {
        "DeviceQuery": {
            "edges": [
                {
                    "node": {
                        "id": "0199ec89-36ec-7c36-b291-98da56704e25",
                        "imei": "<Your device IMEI>"
                    }
                }
            ]
        }
    }
}
```

***

