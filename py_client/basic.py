import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

# -> API (Application Programming Interface)
# rest api / a web based api by using http request

get_response = requests.post(endpoint, json={"title": "ABC123", "content": "Hello World", "price": 123})  # HTTP Request
# print(get_response.text)  # raw text response
# print(get_response.status_code)

"""
HTTP REQUEST -> HTML
REST API HTTP REQUEST -> JSON (JavaScript Object Notation) ~ Pyhton Dict
"""

print(get_response.json())  # -> prints as Py Dict

"""
{
    "args": {},
    "data": "",
    "files": {},
    "form": {},
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.32.3",
        "X-Amzn-Trace-Id": "Root=1-683ec94c-2e0c61ce0fc3fcc849313ce2",
    },
    "json": None,
    "method": "GET",
    "origin": "176.74.142.237",
    "url": "https://httpbin.org/anything",
}
"""
