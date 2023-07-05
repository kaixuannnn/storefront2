from django.shortcuts import render
from store.models import Customer
from django.db.models import Value, F, Count

def say_hello(request):
   queryset = Customer.objects.annotate(order_count=Count('order__id'))
   return render(request, 'hello.html', {'name': 'Mosh', 'products': queryset})
