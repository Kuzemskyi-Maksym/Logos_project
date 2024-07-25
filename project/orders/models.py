from django.db import models

from accounts.models import User
from main.models import Products

"""
Модель Order
user: Зв'язок з моделлю User. Якщо користувача видалять, поле буде встановлене в None за замовчуванням.
created_timestamp: Дата і час створення замовлення.
phone_number: Номер телефону покупця.
requires_delivery: Флаг, що вказує на необхідність доставки.
delivery_address: Адреса доставки, якщо потрібна доставка.
payment_on_get: Флаг, що вказує, чи буде оплата при отриманні.
is_paid: Флаг, що вказує, чи замовлення оплачено.
status: Статус замовлення, за замовчуванням "In processing".
Модель OrderItem
order: Зв'язок з моделлю Order.
product: Зв'язок з моделлю Products. Якщо продукт видалять, поле буде встановлене в None за замовчуванням.
name: Назва продукту.
price: Ціна продукту.
quantity: Кількість продукту в замовленні.
created_timestamp: Дата і час додавання товару до замовлення.
Клас OrderitemQueryset
total_price: Обчислює загальну ціну всіх товарів в замовленні.
total_quantity: Обчислює загальну кількість товарів в замовленні.
"""

class OrderitemQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    requires_delivery = models.BooleanField(default=False)
    delivery_address = models.TextField(null=True, blank=True)
    payment_on_get = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='In processing')

    class Meta:
        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ("id",)

    def __str__(self):
        return f"Order № {self.pk} | Buyer {self.user.first_name} {self.user.last_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, default=None)
    name = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Date of sale")

    class Meta:
        db_table = "order_item"
        verbose_name = "Sold good"
        verbose_name_plural = "Sold goods"
        ordering = ("id",)

    objects = OrderitemQueryset.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Item {self.name} | Ordering № {self.order.pk}"
