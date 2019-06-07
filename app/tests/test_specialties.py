from .common import query, response_json


def test_specialties():
    response = query("/specialties")

    assert response.status_code == 200

    data = response_json(response)

    assert "specialties" in data
    assert len(data["specialties"]) == 75


def test_specialties_with_size():
    response = query("/specialties?size=10")

    assert response.status_code == 200

    data = response_json(response)

    assert "specialties" in data
    assert len(data["specialties"]) == 10


def test_specialties_size_param_bad_type():
    response = query("/specialties?size=abc")

    assert response.status_code == 400

    data = response_json(response)

    assert data["error"] == "'size' must be a positive int"


def test_specialties_size_param_positive_int():
    response = query("/specialties?size=0")

    assert response.status_code == 400

    data = response_json(response)

    assert data["error"] == "'size' must be a positive int"
