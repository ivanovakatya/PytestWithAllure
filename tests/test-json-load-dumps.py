# import requests
import json
# import pytest
# import jsonpath



def test_loads_dumps ():
    a = {
        "product" : "samsung",
        "price" : 20
    }
    print ("Dictionary = ", a)

    a_json_dumps = json.dumps(a)
    print ("Json dumps = ", a_json_dumps)

    a_loads = json.loads(a_json_dumps)
    print ("Json loads = ", a_loads)

    print(a == a_loads)

    print (a == a_json_dumps)


    print (a_json_dumps == a_loads)


