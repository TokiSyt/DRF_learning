import requests

headers = {"Authorization": "Bearer a92a31110592da1d718d44a1f8d7881ed44fb9ef"}
endpoint = "http://localhost:8000/api/products/20/update/"

data = {
    "title": "test from client",
    "content": "test from client",
}

put_response = requests.put(endpoint, json=data, headers=headers)

print("Status code:", put_response.status_code)
try:
    print(put_response.json())
except requests.exceptions.JSONDecodeError:
    print("Response is not valid JSON.")
