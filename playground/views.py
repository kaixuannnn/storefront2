from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem


def say_hello(request):
   query_set = Product.objects.prefetch_related('promotions').all()
   return render(request, 'hello.html', {'name': 'Mosh', 'products': list(query_set)})
