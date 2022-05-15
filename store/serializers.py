from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection
from django.db.models.aggregates import Count


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']

    product_count = serializers.SerializerMethodField('product_per_collection')

    def product_per_collection(self, collection: Collection):
        result = Product.objects.filter(collection__id=collection.id).aggregate(count=Count('id'))
        return result['count']
        # return collection.objects.aggregate(count=Count('id'))


class ProductSerializer(serializers.ModelSerializer):  # change base class to 'ModelSerializer'
    class Meta:
        model = Product
        # fields = to an array or tuples  of fields in product class we wane include here
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
