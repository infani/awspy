import boto3
from datetime import datetime
import json
import requests


def getApiKey(apiId: str):
    client = boto3.client('appsync')
    res = client.list_api_keys(
        apiId=apiId
    )
    for key in res['apiKeys']:
        expiredTime = datetime.fromtimestamp(key['expires'])
        now = datetime.now()
        if now < expiredTime:
            return str(key['id'])
    raise Exception('appsync key is not found')


class appsync:
    def __init__(self, endpoint: str, apiId: str) -> None:
        self.endpoint = endpoint
        self.apiId = apiId
        apiKey = getApiKey(apiId)
        self.headers = {'x-api-key': apiKey}

    def query(self, query, variables):
        data = json.dumps(
            {
                "query": query,
                "variables": variables
            }
        )

        res = requests.post(
            url=self.endpoint,
            headers=self.headers,
            data=data.encode('utf8')
        )
        return res.json()
