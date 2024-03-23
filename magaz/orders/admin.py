from django.contrib import admin

from orders.models import Order, OrderItem


# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'created_timestamp', 'phone_number', 'requires_delivery', 'delivery_address', 'payment_on_get',
        'is_paid',
        'status')


admin.site.register(OrderItem)
