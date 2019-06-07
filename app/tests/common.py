import json
from www import server


def make_test_client():
    flask_app = server.create()
    test_client = flask_app.test_client()
    return test_client


def query(url):
    test_client = make_test_client()
    return test_client.get(url)


def response_json(res):
    return json.loads(res.get_data(as_text=True))
