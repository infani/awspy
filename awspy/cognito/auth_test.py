from awspy.cognito.auth import Auth
from awspy.config import Config

def test_Auth():
    cfg = Config()
    clientID = cfg.cognitoClientID
    username = cfg.username
    password = cfg.password
    try:
        auth = Auth(clientID)
        accessToken = auth.login(username, password)
        print(accessToken)
    except Exception as e:
        print(e)