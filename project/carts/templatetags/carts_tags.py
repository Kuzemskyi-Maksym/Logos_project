from django import template

from carts.models import Cart

register = template.Library()

"""
user_carts: Це функція, яка перевіряє, чи є користувач автентифікованим:

Якщо так, вона повертає кошики для автентифікованого користувача.
Якщо користувач не автентифікований, вона створює новий сеанс (якщо ще не створено) і повертає кошики, пов'язані з цим сеансом.
"""


@register.simple_tag()
def user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)

    if not request.session.session_key:
        request.session.create()

    return Cart.objects.filter(session_key=request.session.session_key)
