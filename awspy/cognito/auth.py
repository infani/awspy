import boto3


class Auth:
    def __init__(self, clientId) -> None:
        self.clientId = clientId

    def login(self, username, password):
        cli = boto3.client('cognito-idp')
        res = cli.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password},
            ClientId=self.clientId)
        print(res)
