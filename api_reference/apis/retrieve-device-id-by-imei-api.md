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
POST https://api.example-platform.com/fleet/graphql/DeviceQuery
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
  "query": "query DeviceQuery($where: DeviceWhereInput) { DeviceQuery(where: $where) { edges { node { id imei name } } } }",
  "variables": {
    "where": {
      "imei": "867451039284561"
    }
  },
  "operationName": "DeviceQuery"
}'
```

### Example Request Body (Payload)

Here is the JSON payload representing the GraphQL request:

```json
{
  "query": "query DeviceQuery($where: DeviceWhereInput) { DeviceQuery(where: $where) { edges { node { id imei name } } } }",
  "variables": {
    "where": {
      "imei": "867451039284561"
    }
  },
  "operationName": "DeviceQuery"
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
            "id": "c1b9e2a4-6f23-4c91-bb4a-0c8f1d9e6a52",
            "imei": "867451039284561",
            "name": "Vehicle-Camera-Unit-12"
          }
        }
      ]
    }
  }
}
```

***

