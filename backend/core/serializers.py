from rest_framework import serializers
from .models import Products

class ProductsSerialize(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = (
                    'id',
                    'name',
                    'description',
                    'price'
                )
