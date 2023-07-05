from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # We can do this way to retrieve object, however we need to do error handling, therefore
    # try: 
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    # We can use filter, as it return querySet and when we ask for first, it will return null
    # product = Product.objects.filter(pk=0).first()
    # we also can check the existence of the object
    query_set = Product.objects.filter(title__icontains='coffee')
    
    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(query_set)})
