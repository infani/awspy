
import os

class Config:
    region = os.getenv("AWS_DEFAULT_REGION", "ap-northeast-1")
    cognitoUserPoolID = os.getenv("cognitoUserPoolID", "")
    cognitoClientID = os.getenv("cognitoClientID", "")
    username = os.getenv("username", "")
    password = os.getenv("password", "")
