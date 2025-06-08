import json
from django.forms.models import model_to_dict

# from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

""" Manual Way
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
         fields=['id', 'title', 'price'])
        return JsonResponse(data)
        data = model_to_dict(model_data,
        # model instance (model_data)
        # turn into a python dict
        # return Json to client
"""


@api_view(["GET"])  # choosing method to allow only what we want to
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(instance, fields=["id", "title", "price", "sale_price"])
        data = ProductSerializer(instance).data
    return Response(data)
