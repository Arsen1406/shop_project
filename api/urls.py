from django.urls import path, include
from rest_framework import routers
from .views import ItemsViewSet, BuyViewSet

router = routers.DefaultRouter()
router.register(r'item', ItemsViewSet)
router.register(r'^buy/(?P<item_id>\d+)', BuyViewSet, basename='buy_item')

urlpatterns = [
    path('', include(router.urls))
]
