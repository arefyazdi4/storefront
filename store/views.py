from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


@api_view()
def product_list(request):
    query_set = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(
        query_set, many=True, context={'request': request})  # using context to pass extra stuff
    return Response(serializer.data)


@api_view()
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)  # model object
        serializer = ProductSerializer(product, context={'request': request})  # serializer.data->dict object
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view()
def collection_detail(request, pk):
    return Response('ok')
