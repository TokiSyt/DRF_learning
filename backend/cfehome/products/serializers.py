from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ["title", "content", "price", "sale_price", "my_discount"]

    def get_my_discount(self, obj): #to change the representation
        # obj.user -> user.username
        # obj.category -> category.etc
        if not hasattr(obj, 'id') and not isinstance(obj, Product):
            return None
        return obj.get_discount()
