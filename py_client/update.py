import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Updated Product Title",
    "content": "Updated content",
    "price": 229.99
}

put_response = requests.put(endpoint, json=data)

print("Status code:", put_response.status_code)
try:
    print(put_response.json())
except requests.exceptions.JSONDecodeError:
    print("Response is not valid JSON.")
