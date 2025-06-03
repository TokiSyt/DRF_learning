import requests

#endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

# -> API (Application Programming Interface)
# rest api / a web based api by using http request

get_response = requests.get(endpoint)  # HTTP Request
print(get_response.text)  # raw text response

"""
HTTP REQUEST -> HTML
REST API HTTP REQUEST -> JSON (JavaScript Object Notation) ~ Pyhton Dict
"""

print(get_response.json()) # -> prints as Py Dict

'''
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
'''

print(get_response.status_code)