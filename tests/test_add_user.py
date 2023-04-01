import requests
import pytest


@pytest.fixture
def fixture_code(scope="module"):
        global user_data
        user_data = open('user_data.json', 'r')
        yield
        user_data.close()

def test_add_new_student (fixture_code):
        url = "http://127.0.0.1:8000/product"

        response = requests.post(url, user_data)
        print("Content: ", response.content)

        assert response.status_code == 201