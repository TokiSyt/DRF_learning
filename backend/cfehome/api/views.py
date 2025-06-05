import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body #byte string of body data
    data = {}
    print(request.GET)
    print(request.POST)
    try:
        data = json.loads(body) #string of JSON Data -> Python Dict
    except:
        pass
    print(data.keys())
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data['params'] = request.GET
    return JsonResponse(data)