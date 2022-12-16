import boto3
from datetime import datetime


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