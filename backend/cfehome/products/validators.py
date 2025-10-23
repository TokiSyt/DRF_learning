from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import Product

def validate_title(value):
        qs = Product.objects.filter(title__iexact=value)
        
        #iexact . case insensitive
        
        if qs.exists():
            raise serializers.ValidationError(
                f"'{value}' is already being used in another product title."
            )
        return value
    
unique_product_title = UniqueValidator(queryset=Product.objects.all())