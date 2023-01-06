import boto3
import requests
from jose import jwt

class Auth:
    def __init__(self, region: str, userPoolID: str, clientId: str) -> None:
        self.clientId = clientId
        jwks_url = f'https://cognito-idp.{region}.amazonaws.com/{userPoolID}/.well-known/jwks.json'
        self.jwks = requests.get(jwks_url).json()
        # print(self.jwks)

    def login(self, username: str, password: str):
        cli = boto3.client('cognito-idp')
        res = cli.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password},
            ClientId=self.clientId)
        accessToken = res['AuthenticationResult']['AccessToken']
        # print(accessToken)
        return accessToken

    def decodeJWT(self, token: str):
        res = jwt.decode(token, self.jwks)
        return res['sub']
