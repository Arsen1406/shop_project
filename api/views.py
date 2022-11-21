from rest_framework import viewsets, views, status
from django.shortcuts import get_object_or_404, redirect

from pay_app.models import Item
from pay_app.create_price import create_product

from .serializers import ItemSerializer


class ItemsViewSet(viewsets.ModelViewSet):
    """Все товары."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class BuyViewSet(viewsets.ViewSetMixin):
    """Покупка товара."""

    def get(self, pk):
        item = get_object_or_404(Item, id=pk)
        session = create_product(item)
        return redirect(session.url, status=status.HTTP_200_OK)
