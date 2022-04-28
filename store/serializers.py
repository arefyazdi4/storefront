from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):  # change base class to 'ModelSerializer'
    class Meta:
        model = Product
        # fields = to an array or tuples  of fields in product class we wane include here
        fields = ['id', 'title', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail'  # this argument is used for generating hyper links
        # we need to creat a view and url by this name
    )                  # fourth method

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
