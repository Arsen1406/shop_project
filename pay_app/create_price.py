import stripe

stripe.api_key = 'sk_test_51LhdVjKk8h0TMPQxhT8SaAewlIn0g0ZsUQefwDvHMZRumD1SK21EX2zk7LvEiBZqBPH9tROoPbhYiL9hlEQGTwks00hfBkin78'


def create_product(item):
    convert = item.price * 100
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(convert),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )
    return session
