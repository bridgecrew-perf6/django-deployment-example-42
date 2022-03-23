from django import template

register = template.Library()


@register.filter(name='cut_1')
def cut_1(value, arg):
    return value.replace(arg, '')
