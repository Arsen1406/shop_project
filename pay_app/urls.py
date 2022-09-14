from django.urls import path
from . import views


app_name = 'pay_app'

urlpatterns = [
    path('', views.shop_all_items, name='all_items'),
    path('buy/<int:item_id>/', views.buy, name='buy'),
    path('item/<int:item_id>/', views.item, name='item'),
]
