from django import template

register = template.Library()

CURRENCY_SYMBOLS = {
    'rub': 'руб.',
    'usd': "$"
}


@register.filter()
def currency(value, code = 'rub'):
    postfix = CURRENCY_SYMBOLS[code]

    return f'{value}{postfix}'
