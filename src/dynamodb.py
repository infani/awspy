import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DevicePushedInfo-vtib2crdejecxibzdt5rlklw44-dev')
# table.update_item(Key={'mac': '000000000000'},UpdateExpression='SET online = :val1',ExpressionAttributeValues={':val1': False})
response = table.get_item(Key={'mac': '000000000000'})
item = response['Item']
print(item)