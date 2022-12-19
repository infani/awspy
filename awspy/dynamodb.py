import boto3


class dynamodb:
    def __init__(self, tableName: str) -> None:
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(tableName)


    def getItem(self, key):
        res = self.table.get_item(
            Key=key
        )
        return res['Item']
