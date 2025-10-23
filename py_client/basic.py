import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" #get_response
endpoint = "http://localhost:8000/api/" #post_response

#get_response = requests.get(
#    endpoint, params={"abc": 123}, json={"query": "Hello world"}
#)
post_response = requests.post(endpoint, json={"title": "big title", "content": "Hello World"})  # HTTP Request
# print(get_response.text)
# print(get_response.status_code)
print(post_response.json())
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
