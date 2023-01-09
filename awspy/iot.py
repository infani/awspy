import boto3
import json

class shadow:
    def __init__(self, thingName: str, shadowName: str) -> None:
        self.thingName = thingName
        self.shadowName = shadowName
        self.client = boto3.client('iot-data')

    def set(self, payload: str):
        self.client.update_thing_shadow(thingName=self.thingName, shadowName=self.shadowName, payload=bytes(payload, 'utf-8'))

    def get(self):
        res = self.client.get_thing_shadow(thingName=self.thingName, shadowName=self.shadowName)
        payload = res['payload']
        
        return json.loads(payload.read())
