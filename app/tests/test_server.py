from .common import query


def test_index():
    response = query("/")

    assert response.status_code == 200
    assert b"Hello World" in response.data
