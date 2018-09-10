from app import app
import json
import pytest


@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)
    return test_client


def post_json(client, url, json_dict):
    # Send dictionary json_dict as a json to the specified url
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')


def json_of_response(response):
    # Decode json from response
    return json.loads(response.data.decode('utf8'))


#  #  #  #  #  #  #  #  #  #  #  #  TESTS  #  #  #  #  #  #  #  #  #  #


def test_index(client):
    response = client.get('/')
    assert b'Basic REST API' in response.data


def test_get_all(client):
    response = client.get('/person')
    assert b'1', b'2' in response.data


def test_get(client):
    response = client.get('/person/1')
    assert b'1' in response.data


def test_add(client):
    response = post_json(client, '/person', {
        'id': '4',
        'name': 'Tester',
        'work': 'Testing'})
    assert response.status_code == 200
