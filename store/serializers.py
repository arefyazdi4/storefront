from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail'  # this argument is used for generating hyper links
        # we need to creat a view and url by this name
    )                  # fourth method
    # collection = CollectionSerializer()  # third method
    # collection = serializers.PrimaryKeyRelatedField(  # first method
    #     queryset=Collection.objects.all()
    # )
    # collection = serializers.StringRelatedField()  # second method

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
