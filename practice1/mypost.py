import json
import requests

URL = "http://127.0.0.1:8000/user/customer_create/"
data = {
    'name': 'Pritesh',
    'serial_id': 11,
    'site': 'remote',
}
json_data = json.dumps(data)
print(json_data)

r = requests.post(url = URL, data = json_data)
print(r)
print(r.json)
# print("hello")
# # print(r.text)
# data1 = r.json()
# this error is not solved , it says that -->   json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
# print(data1)