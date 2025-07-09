# Usually stays in views.py

from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    get -> list -> queryset
    get -> retrieve -> Product instance Detail View
    post -> create -> new instance
    put -> total update
    patch -> partial update
    delete -> destroy
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # default


class ProductGenericViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    get -> list -> queryset - mixins.ListModelMixin
    get -> retrieve -> Product instance Detail View - mixins.RetrieveModelMixin
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # default
