from django import template

register = template.Library()

@register.filter
def currency_vn(value):
    try:
        if value is None:
            return ""
        # Format with comma as thousands separator then replace with dot
        formatted = "{:,.0f}".format(float(value))
        return formatted.replace(',', '.') + ' đ'
    except (ValueError, TypeError):
        return value
