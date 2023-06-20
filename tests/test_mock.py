import json
import pytest


def test_resource_100(client):
    response = client.get("/resource?data=100")
    expect_response = [{"age":"30","id":"100","name":"jack"},{"age":"32","id":"101","name":"jill"}]
    assert json.loads(response.data) == expect_response

def test_resource_200(client):
    response = client.get("/resource?data=200")
    expect_response = [{'age': '40', 'id': '200', 'name': 'tom'}, {'age': '28', 'id': '201', 'name': 'jerry'}]
    assert json.loads(response.data) == expect_response

def test_resource_non_exist_file(client):
    response = client.get("/resource?data=non_exist_file")
    expect_response = []
    assert json.loads(response.data) == expect_response

@pytest.mark.parametrize("code, status_name", 
                         [(200, "OK"), 
                          (301, "MOVED_PERMANENTLY"),
                          (403, "FORBIDDEN"),
                          (404, "NOT_FOUND"),
                          (500, "INTERNAL_SERVER_ERROR"),
                          (503, "SERVICE_UNAVAILABLE"),
                          (504, "GATEWAY_TIMEOUT"),
                          (999, "is not a valid HTTPStatus")
                          ])
def test_status(client, code, status_name):
    response = client.get(f"/status?code={code}")
    assert response.data.decode('utf-8') == f"{code} {status_name}"
    assert response.status_code == code

@pytest.mark.parametrize("ms", [0, 1, 2, 100, 1000, 2000, 3000])
def test_delay(client, ms):
    response = client.get(f"delay?ms={ms}")
    assert f"{ms}" in response.data.decode('utf-8')