from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def product_list(request):
    api_response_ok = Response('ok')
    print('api respond ok\n', api_response_ok)
    print('....')
    return api_response_ok


@api_view()
def product_detail(request, id):
    return Response(id)
