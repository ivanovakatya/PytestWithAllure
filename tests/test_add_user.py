import requests
import json
import pytest
import jsonpath
# from faker import Faker

# fake = Faker()

# def test_get_user_data():
#         response = requests.get("http://127.0.0.1:8000/user/me%22)
#         assert response.status_code == 200

@pytest.fixture
def fixture_code(scope="module"):
        global user_data
        user_data = open('./user_data.json', 'r')
        yield
        user_data.close()

def test_add_new_student (fixture_code):
        headers = { 
                'accept' : "application/json",
                'Content-Type':"application/json"
                }
        url = "http://127.0.0.1:8000/users"
        request_json = json.loads(user_data.read())
        print("Json: ", request_json)
        # request_json['username'] = "hello"
        # request_json['password_hash'] = "hello"
        # print (request_json['username'], request_json['password_hash'])
        response = requests.post(url, request_json, headers=headers)

        print("Content: ", response.content)

        assert response.status_code == 201