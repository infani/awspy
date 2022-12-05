import boto3
import requests
from jose import jwt

class Auth:
    def __init__(self, region: str, userPoolID: str, clientId: str) -> None:
        self.region = region
        self.userPoolID = userPoolID
        self.clientId = clientId

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
        jwks_url = f'https://cognito-idp.{self.region}.amazonaws.com/{self.userPoolID}/.well-known/jwks.json'
        jwks = requests.get(jwks_url).json()
        # print(jwks)
        res = jwt.decode(token, jwks)
        return res['sub']
