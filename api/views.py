from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import get_object_or_404, redirect

from pay_app.models import Item
from pay_app.create_price import create_product

from .serializers import ItemSerializer, BuySerializer


class ItemsViewSet(viewsets.ModelViewSet):
    """Все товары."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class BuyViewSet(viewsets.ModelViewSet):
    """Покупка товара."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request):
        item = get_object_or_404(Item, id=self.kwargs.get('item_id'))
        session = create_product(item)
        return session.url
