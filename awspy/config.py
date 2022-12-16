from awspy import cloudmap
import os


def getConfig(service: str):
    res = cloudmap.discover_instances('vsaas', service)
    return res['Instances'][0]['Attributes']


class Config:
    region = os.getenv("AWS_REGION", "ap-northeast-1")
    username = os.getenv("username", "")
    password = os.getenv("password", "")

    cognitoUserPoolID = os.getenv("cognitoUserPoolID", "")
    cognitoClientID = os.getenv("cognitoClientID", "")
    vortexaiConfig = getConfig('vortexai')
    if "cognitoUserPoolID" in vortexaiConfig:
        cognitoUserPoolID = vortexaiConfig["cognitoUserPoolID"]
    if "cognitoClientID" in vortexaiConfig:
        cognitoClientID = vortexaiConfig["cognitoClientID"]

    amplifyDBConfig = getConfig('amplify')
    appsyncID = ''
    appsyncUrl=""
    if "appsyncID" in amplifyDBConfig:
        appsyncID = amplifyDBConfig["appsyncID"]
    if "appsyncUrl" in amplifyDBConfig:
        appsyncUrl = amplifyDBConfig["appsyncUrl"]


config = Config()
