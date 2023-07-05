from django.shortcuts import render
from store.models import Product
from django.db.models import Count

def say_hello(request):
   result = Product.objects.aggregate(count=Count('id'))
   return render(request, 'hello.html', {'name': 'Mosh', 'result': result})
