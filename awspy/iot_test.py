from awspy import iot
import json

def test_shadow():
    thingName = 'test_updateShadow'
    shadowName = 'feedback'
    feebackShadow = iot.shadow(thingName, shadowName)
    payload = {
        "state": {
            "desired": {
                "test": "test"
            }
        }
    }
    feebackShadow.set(json.dumps(payload))
    res = feebackShadow.get()
    assert res['state']['desired']['test'] == 'test'