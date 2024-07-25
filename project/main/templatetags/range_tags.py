from django import template

register = template.Library()

"""
times: Цей фільтр використовує значення, щоб створити об'єкт range, який використовується в шаблоні для створення зірок у рейтинговій системі.

to_int: Цей фільтр перетворює значення на ціле число. Якщо значення не може бути перетворене в ціле число, повертає 0.
"""

@register.filter
def times(value):
    try:
        value = int(value)
        return range(value)
    except (ValueError, TypeError):
        return range(0)

@register.filter
def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0

