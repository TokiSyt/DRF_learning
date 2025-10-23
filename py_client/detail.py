import requests

endpoint = "http://localhost:8000/api/products/20/"

get_response = requests.get(endpoint, json={"title": "ABC123", "content": "Hello World", "price": 123})


print(get_response.json())  # -> prints as Py Dict

