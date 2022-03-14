from django import template
from order.models import CartItem, Order

register = template.Library()

@register.filter
def total_order_count():
    total_order_number = CartItem.objects.all().count()

    return total_order_number
