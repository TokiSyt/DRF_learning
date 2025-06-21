from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

"""
Generic API Views for CRUD operations:

# CREATE: generics.CreateAPIView 
# READ: generics.ListAPIView (multiple), generics.RetrieveAPIView (single)  
# UPDATE: generics.UpdateAPIView
# DELETE: generics.DestroyAPIView
"""

from .models import Product
from .serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)

        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title

        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):  # GET requests - Single Item
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' -> Products.object.get(pk='abc')


class ProductUpdateAPIView(generics.UpdateAPIView):  # GET requests - Single Item
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # -> Products.object.get(pk='abc')

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # -> Products.object.get(pk='abc')

    def perform_destroy(self, instance):
        # instance if any change is needed
        super().perform_destroy(instance)


# class ProductListAPIView(generics.ListAPIView):  # GET requests - Multiple Items
#     """
#     Not gonna use

#     # Handles GET requests - Multiple / all products in this case
#     """

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup_field = 'pk' -> Products.object.get(pk='abc')

# ---------------------------------------------------------------------------------------------------#


class ProductMixinView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):  # HTTP -> GET
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs): #HTTP -> POST
        return self.create(request, *args, **kwargs)


# ---------------------------------------------------------------------------------------------------#

# @api_view(["GET", "POST"])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == "GET":
#         if pk is not None:
#             # detail view

#             # queryset = Product.objects.filter(pk=pk)
#             # if not queryset.exists()

#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data  # false for many is default
#             return Response(data)

#         else:
#             queryset = Product.objects.all()  # or qs
#             data = ProductSerializer(queryset, many=True).data
#             return Response(data)

#             # url_args
#             # get request -> detail view
#             # list view

#     if method == "POST":
#         # Create an item
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get("title")
#             content = serializer.validated_data.get("content") or None

#             if content is None:
#                 content = title

#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({"invalid:" "Not good data"}, status=400)
