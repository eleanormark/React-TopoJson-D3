from .common import query, response_json

def test_physician_count_specialty_name():
    response = query("physician-counts?specialty=:specialty_name")

    assert response.status_code == 400

    data = response_json(response)

    assert data["error"] == "specialty 'abc' does not exist"