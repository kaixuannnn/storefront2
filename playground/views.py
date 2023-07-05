from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem


def say_hello(request):
   # Exersice: We want to find the list of product which had been ordered and sort by title
   # distinct() - to eliminate redundant record
   query_set =  Product.objects.filter(id__in = OrderItem.objects.values_list('product__id').distinct()).order_by('title')
   return render(request, 'hello.html', {'name': 'Mosh', 'products': list(query_set)})
