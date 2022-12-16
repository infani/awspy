from awspy import appsync
from awspy.config import config

def test_getApiKey():
    key = appsync.getApiKey(config.appsyncID)
    assert key.startswith('da') == True
    print(key)