from rest_framework import generics

"""
Generic API Views for CRUD operations:

# CREATE: CreateAPIView 
# READ: ListAPIView (multiple), RetrieveAPIView (single)  
# UPDATE: UpdateAPIView
# DELETE: DestroyAPIView
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
        price = serializer.validated_data.get("price")

        print(serializer.validated_data)
        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):  # Handles GET requests
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' -> Products.object.get(pk='abc')
