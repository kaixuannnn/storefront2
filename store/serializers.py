from rest_framework import serializers
from decimal import Decimal

from store.models import Collection, Product

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # get Primary Key of associated collection
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset = Collection.objects.all()
    # )
    # get String of associated collection
    # collection = serializers.StringRelatedField()
    # get Object of associated collection
    # collection = CollectionSerializer()
    # get Hyperlink of associated collection
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection_detail',
    )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
