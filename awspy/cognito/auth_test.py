from awspy.cognito.auth import Auth

def test_Auth_WrongClientID():
    clientID = 'WrongClientID'
    username = 'username'
    password = 'password'
    try:
        auth = Auth(clientID)
        accessToken = auth.login(username, password)
        print(accessToken)
    except Exception as e:
        assert str(e) == 'An error occurred (ResourceNotFoundException) when calling the InitiateAuth operation: User pool client WrongClientID does not exist.'