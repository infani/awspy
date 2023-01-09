from awspy import iot
import json

def test_shadow():
    thingName = 'test_updateShadow'
    shadowName = 'feedback'
    feedbackShadow = iot.shadow(thingName, shadowName)
    payload = {
        "state": {
            "desired": {
                "test": "test"
            }
        }
    }
    feedbackShadow.set(json.dumps(payload))
    res = feedbackShadow.get()
    assert res['state']['desired']['test'] == 'test'