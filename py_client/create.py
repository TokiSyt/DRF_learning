import requests

headers = {"Authorization": "Bearer 64e095334958595c33c2964eeebb19a09531db79"}
endpoint = "http://localhost:8000/api/products/"

data = {"title": "test", "price": 32.9}
get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())  # -> prints as Py Dict
