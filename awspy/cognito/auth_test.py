from awspy.cognito.auth import Auth, DecodeJWT
from awspy.config import Config

def test_Auth():
    cfg = Config()
    clientID = cfg.cognitoClientID
    username = cfg.username
    password = cfg.password
    try:
        auth = Auth(clientID)
        accessToken = auth.login(username, password)
        print(accessToken)
    except Exception as e:
        print(e)

def test_DecodeJWT():
    cfg = Config()
    jwt = 'eyJraWQiOiJ3ZWh0TkFBQlJuR0RxbDVaT0E5dzZuU2JNU1FBemJSbDZhMTRZNFhXS1IwPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2ZGQ3YzAxZC04YzVmLTRiZDItOTA1Yy00MjBmMWY5Yjk2YTAiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTFfQnhHNEZnckZtIiwiY2xpZW50X2lkIjoiM25jZnVhM29oM3YxM2NqdDFrM25qa25jMHMiLCJvcmlnaW5fanRpIjoiZDk2Y2ZjOWYtMDZmYS00ZmNmLWI1MjMtY2U1M2QwNTYyYTRlIiwiZXZlbnRfaWQiOiIwODFjMTE3YS03MjQ5LTQ1ZDktYTEzNS01NThkNWIwZWEwODUiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjY5ODg0MDY2LCJleHAiOjE2Njk4ODc2NjYsImlhdCI6MTY2OTg4NDA2NiwianRpIjoiNTI2Nzg4MTEtMDkyNy00NjI4LWJhYWEtZmY3Y2NlM2JhN2JmIiwidXNlcm5hbWUiOiI2ZGQ3YzAxZC04YzVmLTRiZDItOTA1Yy00MjBmMWY5Yjk2YTAifQ.r8T-H3tZy99g8GADyI120rPBe9o9CFesJPt-PI-T0Q6qxoc1YtbEH-7n15aRw-UTJofVrF2CajGBfNYZGAbtBua1FGCAN_AvuI4TmGXTidvNnDoB6o3z70l7QRt0U6epBNJq0Aqp212SPnkwlkTvhCDuGB4veBqobDP-E-ZpfHcD-vJPqw9mH_2CUp21Ns-fuOvgV1ys75e0rENc0IhW5mV29MMOZc8KUtnYMK8v7bF3Hh2QCuSKixuUvrZwQWAbJ0nK8yj2sBEX-fHDZrp1rQLGnPRbff_zeRo08upmTbhAvGOi8AVW7pmNc9_DPvRsRc4YfwX6JHpdM961LSs9dw'
    DecodeJWT(cfg.region, cfg.cognitoUserPoolID, jwt)
