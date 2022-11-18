from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from pay_app.models import Item
from rest_framework.validators import UniqueTogetherValidator
from pay_app.create_price import create_product


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price',)


class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = create_product
        fields = ('__all__')
