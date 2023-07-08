from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from . import models
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse


# Register your models here.
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url =reverse('admin:store_product_changelist') + '?' + urlencode({'collection__id': str(collection.id)})
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    # before that, we cannot sort the inventory as we dont know how to sort it, and now by adding this, django know that the column can be sort by inventory
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

@admin.register(models.Customer)
class CustomerAmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at', 'payment_status', 'customer']