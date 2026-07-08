from django import template
from decimal import Decimal

register = template.Library()


@register.filter
def multiply(value, arg):
    if value:
        return Decimal(value) * Decimal(str(arg))
    else:
        return ''
