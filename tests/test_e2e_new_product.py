import requests
import pytest
import json
from faker import Faker

fake = Faker()

def test_get_all_products():
        url = "http://127.0.0.1:8000/products"
        response = requests.get(url)
        assert response.status_code == 200

def test_post_with_faker_data ():
        url = "http://127.0.0.1:8000/product"
        user_data = {
                "name": fake.unique.first_name(),
                "description": fake.prefix(),
                "price": fake.random_int(0, 20)
        }
        
        request_json = json.dumps(user_data)
        response = requests.post(url, request_json)

        json_response = json.loads(response.content)
       
        assert json_response["name"] == user_data["name"]
        assert json_response["description"] == user_data["description"]
        assert json_response["price"] == user_data["price"]
        assert response.status_code == 201

def test_get_product_by_last_id():
        url = "http://127.0.0.1:8000/products"
        response = requests.get(url)
        json_response = json.loads(response.content)
        response_array = []
        for i in json_response:
                response_array.append(i["id"])
        last_element = response_array[- 1]
        url_product = "http://127.0.0.1:8000/product/{}".format(last_element)

        response = requests.get(url_product)
       
        assert response.status_code == 200