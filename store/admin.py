from typing import Any, List, Optional, Tuple
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from tags.models import TaggedItem
from . import models
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        return [
            ('<10', 'Low')
        ]
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any]:
        if self.value() == '<10':
           return queryset.filter(inventory__lt =10)

# Register your models here.
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url =reverse('admin:store_product_changelist') + '?' + urlencode({'collection__id': str(collection.id)})
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']
    search_fields = ['title']


    def collection_title(self, product):
        return product.collection.title

    # before that, we cannot sort the inventory as we dont know how to sort it, and now by adding this, django know that the column can be sort by inventory
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    
    @admin.action(description='Clear inventory')
    def clear_inventory(self, request:HttpRequest, queryset:QuerySet):
       updated_count =  queryset.update(inventory=0)
       self.message_user(
           request,
           f'{updated_count} products were successfully updated.',
           messages.SUCCESS
       )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 10
    list_select_related=['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = reverse('admin:store_order_changelist') + '?' + urlencode({'customer_id': str(customer.id)})
        return format_html('<a href="{}">{}</a>', url, customer.orders_count)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )

class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    min_num = 1
    model = models.OrderItem
    extra = 0

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    autocomplete_fields = ['customer']
    list_display = ['id','placed_at', 'payment_status', 'customer']