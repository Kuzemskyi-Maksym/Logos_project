from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required

from orders.forms import CreateOrderForm
from carts.models import Cart
from orders.models import Order, OrderItem

import logging

"""
Опис Функції create_order
Методи та Логіка
Перевірка POST Запиту:

Якщо запит POST, створюється форма CreateOrderForm з даними POST-запиту.
Перевіряється, чи форма дійсна.
Транзакція:

Використовується transaction.atomic() для забезпечення цілісності даних.
Якщо є елементи в кошику, створюється нове замовлення Order.
Перевірка та Обробка Кошика:

Для кожного елемента в кошику створюється OrderItem і оновлюється кількість продуктів.
Перевіряється, чи не перевищує загальна сума замовлення встановлені межі.
Очищення Кошика:

Після успішного створення замовлення всі елементи в кошику видаляються.
Обробка Помилок:

Якщо виникає ValidationError, помилка записується в журнал і додається до форми.
Всі помилки форми записуються в журнал.
Відповідь:

Після успішної обробки запиту користувач перенаправляється на профіль.
Якщо запит не POST, форма ініціалізується з даними користувача.
"""


logger = logging.getLogger(__name__)

@login_required()
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)
                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'] if form.cleaned_data['requires_delivery'] == '1' else '',
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        total_price = 0
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = product.sell_price()
                            quantity = cart_item.quantity

                            item_total_price = round(price * quantity, 2)
                            if item_total_price > 99999999.99:
                                logger.error(f'Item total price exceeds limit: {name} with total price {item_total_price}')
                                raise ValidationError(f'Total price for item {name} exceeds the limit.')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            # product.quantity -= quantity
                            product.save()

                            total_price += item_total_price

                        if total_price > 99999999.99:
                            logger.error(f'Total order price exceeds limit: {total_price}')
                            raise ValidationError(f'Total order price exceeds the limit.')

                        cart_items.delete()
                        return redirect('accounts:profile')
            except ValidationError as e:
                logger.error(f'Order validation error: {e.message}')
                form.add_error(None, e.message)
        else:
            logger.error(f'Form validation errors: {form.errors}')
            form.add_error(None, 'Please correct the errors below.')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Order placement',
        'form': form,
    }
    return render(request, 'orders/create_order.html', context=context)

