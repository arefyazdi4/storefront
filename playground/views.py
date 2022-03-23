from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import Q, F, DecimalField
from django.db.models import Value, Func, ExpressionWrapper
from store.models import Product, OrderItem, Order, Customer, Collection
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from django.db import transaction
from django.db import connection


def say_hello(request):

    return render(request, 'hello.html', {'name': 'Mosh'})
