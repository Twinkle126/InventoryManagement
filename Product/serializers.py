from rest_framework import serializers
from Product.models import Item


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
