import boto3

def updateShadow(thingName: str, shadowName: str, payload: str):
    client = boto3.client('iot-data')
    res = client.update_thing_shadow(
        thingName=thingName,
        shadowName=shadowName,
        payload=bytes(payload, 'utf-8')
    )
    print(res)
