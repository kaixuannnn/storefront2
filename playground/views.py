from django.forms import DecimalField
from django.shortcuts import render
from store.models import Customer, Product
from django.db.models import Value, F, Count, ExpressionWrapper, DecimalField

def say_hello(request):
   discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
   queryset = Product.objects.annotate(discounted_price=discounted_price)
   return render(request, 'hello.html', {'name': 'Mosh', 'products': queryset})
