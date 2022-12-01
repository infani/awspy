
import os

class Config:
    cognitoClientID = os.getenv("cognitoClientID", "")
    username = os.getenv("username", "")
    password = os.getenv("password", "")
