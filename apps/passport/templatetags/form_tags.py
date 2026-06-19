from django import template
from django.forms import ModelChoiceField

register = template.Library()


@register.filter
def is_foreign_key(field):
    return isinstance(field.field, ModelChoiceField)


@register.filter
def is_moc_list(field):
    return field.name == 'moc_list'
