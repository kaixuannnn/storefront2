from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.models import Product
from store.serializers import ProductSerializer
from django.shortcuts import get_object_or_404


@api_view()
def product_list(request):
    query_set = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(query_set, many=True,  context={'request': request})
    return Response(serializer.data)

@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view()
def collection_detail(request, pk):
    return Response('ok')