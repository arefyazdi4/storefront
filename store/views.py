from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


@api_view()
def product_list(request):
    query_set = Product.objects.all()
    serializer = ProductSerializer(query_set, many=True)
    return Response(serializer)


@api_view()
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)  # model object
        serializer = ProductSerializer(product)  # serializer.data->dict object
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
