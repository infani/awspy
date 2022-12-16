from awspy import appsync
from awspy.config import config


def test_getApiKey():
    key = appsync.getApiKey(config.appsyncID)
    assert key.startswith('da') == True
    print(key)


def test_query():
    cli = appsync.appsync(config.appsyncUrl, config.appsyncID)
    query = """
query GetUser($id: ID!) {
  getUser(id: $id) {
    id
  }
}
    """
    vars = {
        "id": "5cde17ba-cf87-4e09-9946-9cc85d617381"
    }
    res = cli.query(query, vars)
    assert res.ok == True
    assert res.json()['data']['getUser']['id'] == "5cde17ba-cf87-4e09-9946-9cc85d617381"

def test_init():
    appsync.init(config.appsyncUrl, config.appsyncID)
    query = """
query GetUser($id: ID!) {
  getUser(id: $id) {
    id
  }
}
    """
    vars = {
        "id": "5cde17ba-cf87-4e09-9946-9cc85d617381"
    }
    res = appsync.cli.query(query, vars)
    assert res.ok == True