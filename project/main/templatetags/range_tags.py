from django import template

register = template.Library()

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



# from django import template

# register = template.Library()

# @register.filter
# def times(number):
#     return range(number)
