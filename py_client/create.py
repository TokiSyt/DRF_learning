import requests

headers = {"Authorization": "Bearer a92a31110592da1d718d44a1f8d7881ed44fb9ef"}
endpoint = "http://localhost:8000/api/products/"

data = {"title": "test from cliente", "price": 555}
get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())  # -> prints as Py Dict
