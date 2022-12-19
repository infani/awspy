from awspy.dynamodb import dynamodb


def test_dynamodb_getItem():
    tableName = 'Message-vtib2crdejecxibzdt5rlklw44-dev'
    cli = dynamodb(tableName)
    source = '0002D198B5E2-1662453481003'
    key = {
        'source': source,
        'time#index': '1668988800006#487633b7-76fe-4d83-9de5-b743b3da10eb'
    }
    item = cli.getItem(key)
    assert item['source'] == source
    print(item)