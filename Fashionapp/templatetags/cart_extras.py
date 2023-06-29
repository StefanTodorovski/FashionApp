from django import template

register = template.Library()

@register.filter
def total_amount(cart):
    total = sum(item.product.price * item.quantity for item in cart)
    return total


