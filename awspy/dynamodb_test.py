from awspy.dynamodb import dynamodb


def test_dynamodb_getItem():
    tableName = 'Message-vtib2crdejecxibzdt5rlklw44-dev'
    cli = dynamodb(tableName)
    source = "TestData0002D198B5E2-1662453481003"
    key = {
        'source': source,
        'time#index': '1669593704297#f9f6dddb-e573-46e4-87b4-3667c8cf654b'
    }
    item = cli.getItem(key)
    assert item['source'] == source
    print(item)

def test_dynamodb_getItem_KeyError():
    tableName = 'Message-vtib2crdejecxibzdt5rlklw44-dev'
    cli = dynamodb(tableName)
    source = 'KeyError'
    key = {
        'source': source,
        'time#index': '1668988800006#487633b7-76fe-4d83-9de5-b743b3da10eb'
    }
    item = cli.getItem(key)
    
    assert ('source' in item) == False