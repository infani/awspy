from awspy import appsync
from awspy.config import config

def test_getApiKey():
    key = appsync.getApiKey(config.appsyncID)
    print(key)