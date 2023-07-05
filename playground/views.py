from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem, Order


def say_hello(request):
   # Exercise: We want to get the Order query_set to access the associated customer and orderitem and product for the first 5 items
   query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
   return render(request, 'hello.html', {'name': 'Mosh', 'products': list(query_set)})
