import requests
import pytest
import json
from faker import Faker

fake = Faker()


def test_post_with_faker_data ():
        url = "http://127.0.0.1:8000/product"
        user_data = {
                "name": fake.unique.first_name(),
                "description": fake.prefix(),
                "price": fake.random_int(0, 20)
        }
        
        request_json =json.dumps(user_data)
        response = requests.post(url, request_json)

        assert response.status_code == 201