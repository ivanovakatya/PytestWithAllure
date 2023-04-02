import requests
import pytest
import json
import jsonpath
from faker import Faker

fake = Faker()

def test_add_new_product ():

        global id

        url = "http://127.0.0.1:8000/product"
        user_data = {
                "name": fake.unique.first_name(),
                "description": fake.word(),
                "price": fake.random_int(0, 20)
        }
        
        request_json = json.dumps(user_data)
        response = requests.post(url, request_json)

        assert response.status_code == 201

        # print("Response : ", response.text)
        id = jsonpath.jsonpath(response.json(), "id")  


def test_get_new_product_details():              
        url = "http://127.0.0.1:8000/product/" + str(id[0])

        response = requests.get(url)
        assert response.status_code == 200

        # print(response.json())
        formatted_response = json.dumps(response.json(), indent=4)
        print("New product added is: ", formatted_response)
