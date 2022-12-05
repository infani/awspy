from awspy.cognito.auth import Auth
from awspy.config import Config


cfg = Config()
auth = Auth(cfg.region, cfg.cognitoUserPoolID, cfg.cognitoClientID)

def test_Auth():
    username = cfg.username
    password = cfg.password
    try:
        accessToken = auth.login(username, password)
        print(accessToken)
    except Exception as e:
        print(e)


def test_decodeJWT():
    jwt = 'eyJraWQiOiJ3ZWh0TkFBQlJuR0RxbDVaT0E5dzZuU2JNU1FBemJSbDZhMTRZNFhXS1IwPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2ZGQ3YzAxZC04YzVmLTRiZDItOTA1Yy00MjBmMWY5Yjk2YTAiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTFfQnhHNEZnckZtIiwiY2xpZW50X2lkIjoiM25jZnVhM29oM3YxM2NqdDFrM25qa25jMHMiLCJvcmlnaW5fanRpIjoiZTljZTUzYmMtMTU3Ny00OGI2LTllZGQtOTQxODM2ZDAwYzcyIiwiZXZlbnRfaWQiOiIwMTM0MDkzMi0wZWU5LTRhY2MtOTMzNy04YTI1M2Q0YWVmNjIiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjY5OTcwNDI2LCJleHAiOjE2Njk5NzQwMjYsImlhdCI6MTY2OTk3MDQyNiwianRpIjoiMDllYjJhZGMtOTFiYy00N2U0LTllNDQtZWJiOGNkYTk0YTk1IiwidXNlcm5hbWUiOiI2ZGQ3YzAxZC04YzVmLTRiZDItOTA1Yy00MjBmMWY5Yjk2YTAifQ.FqmOwum-XCcJ5n6Wtw5m7oMs337fX_nJrG-2kjiOerNFx2yvYGisr5cgPf1g2p-NHzuAZo91SQyc55oFhGqfmOM8R-vrYAnSVCfZgpWHr8_eeRw348UBaeUgf_uvTCBRsEOOlaWu0IV5_iBYS8AyJwr70WLhNr63HTjIFXZpXO8v9R_mDVdqzeqLVTgn4odFmkYkpPvtnsT_OPBxHEjeX9HbOHZh5kFM9JsGuaXU7W0K-OvKaeolSe8Q5rUwTBwmyMlH0CqmYYDEIHidX77FmVQodCKYtqFaKGVN3VlKc6mRhfUL3Y1z5_Q0DikHXPcFZkaqCHfv-8nYVVjJJYviwg'
    try:
        auth.decodeJWT(jwt)
    except Exception as e:
        print(e)
