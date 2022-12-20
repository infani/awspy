import boto3
from botocore.exceptions import ClientError


class dynamodb:
    def __init__(self, tableName: str) -> None:
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(tableName)

    def getItem(self, key):
        try:
            res = self.table.get_item(
                Key=key
            )
            return res['Item']
        except KeyError as e:
            print(e)
        except ClientError as e:
            print(e)
        return {}
