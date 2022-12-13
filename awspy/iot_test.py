from awspy import iot
import json

def test_updateShadow():
    payload = {
        "state": {
            "desired": {
                "welcome": "aws-iot"
            },
            "reported": {
                "welcome": "aws-iot"
            }
        }
    }
    iot.updateShadow('test_updateShadow', 'feedback', json.dumps(payload))
