from django.forms import DecimalField
from django.shortcuts import render
from store.models import Customer, Product, Collection
from django.db.models import Value, F, Count, ExpressionWrapper, DecimalField
from django.contrib.contenttypes.models import ContentType

from tags.models import TaggedItem

def say_hello(request):
   return render(request, 'hello.html', {'name': 'Mosh'})
