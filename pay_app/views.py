from django.shortcuts import redirect, render
from .models import Item
from .create_price import create_product


def shop_all_items(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    template = 'pay_app/all_items.html'
    return render(request, template, context)

def buy(request, item_id):
    item = Item.objects.get(id=item_id)
    session = create_product(item)
    return redirect(session.url, code=303)


def item(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'item': item,
    }
    template = 'pay_app/item.html'
    return render(request, template, context)
