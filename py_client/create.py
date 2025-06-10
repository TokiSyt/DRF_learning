import requests

endpoint = "http://localhost:8000/api/products/"

data = {"title": "test", "price": 32.9}
get_response = requests.post(endpoint, json=data)

print(get_response.json())  # -> prints as Py Dict
