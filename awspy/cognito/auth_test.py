from awspy.cognito.auth import Auth

def test_Auth():
    clientID = 'clientID'
    username = 'username'
    password = 'password'
    auth = Auth(clientID)
    auth.login(username, password)