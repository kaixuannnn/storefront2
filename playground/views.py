from django.shortcuts import render
from store.models import Customer
from django.db.models import Value, F

def say_hello(request):
   queryset = Customer.objects.annotate(new_id=F('id')+1)
   return render(request, 'hello.html', {'name': 'Mosh', 'products': queryset})
