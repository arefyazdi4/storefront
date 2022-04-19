from django.shortcuts import render
from django.http import HttpResponse


def product_list(request):
    respond_ok = HttpResponse('ok')
    print(respond_ok)
    return respond_ok


