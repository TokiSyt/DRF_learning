from rest_framework.reverse import reverse
from .validators import validate_title
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    #    email = serializers.EmailField(write_only=True)

    title = serializers.CharField(validators=[validate_title])

    class Meta:
        model = Product
        fields = [
            "url",
            "edit_url",
            #            "email",
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            "discount",
        ]

    # def create(self, validated_data):
    # email = validated_data.pop('email')
    # obj = super().create(validated_data)
    # print(email, obj)
    # return obj

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None

        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
