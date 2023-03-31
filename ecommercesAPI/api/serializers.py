from rest_framework import serializers
from . models import *
from django.db.models import Sum,Count


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'price', 'on_discount', 'discount_price',
                  'category', 'stock', 'description']
    
    
    def to_representation(self, instance):
        rep = super(ItemSerializer, self).to_representation(instance)
        rep['category'] = instance.category.name
        return rep