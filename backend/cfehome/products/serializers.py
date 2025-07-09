from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    my_discount = serializers.SerializerMethodField(read_only=True)
    sale_event = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(  # HyperlinkedIdentityField only works in a Model Serializer and SerializerMethodField works anywhere in Serializers
        view_name="product-detail", lookup_field="pk"
    )

    class Meta:
        model = Product
        fields = [
            "url",
            "edit_url",
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
            "sale_event",
        ]

    def get_edit_url(self, obj):
        request = self.context.get("request")  # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):  # to change the representati on
        # obj.user -> user.username
        # obj.category -> category.etc
        if not hasattr(obj, "id") and not isinstance(obj, Product):
            return None
        return obj.get_discount()

    def get_sale_event(self, obj):
        if not hasattr(obj, "id") or not isinstance(obj, Product):
            return None
        return obj.get_sale_event()
