import boto3
import requests
from jose import jwt


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
        accessToken = res['AuthenticationResult']['AccessToken']
        # print(accessToken)
        return accessToken

def DecodeJWT(region: str, userPoolID: str, token: str):
    jwks_url = f'https://cognito-idp.{region}.amazonaws.com/{userPoolID}/.well-known/jwks.json'
    jwks = requests.get(jwks_url).json()
    # print(jwks)
    res = jwt.decode(token, jwks)
    return res['sub']
