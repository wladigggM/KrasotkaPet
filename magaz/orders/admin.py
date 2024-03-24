from django.contrib import admin

from orders.models import Order, OrderItem


# Register your models here.

class OrderItemTabularAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", 'price', 'quantity'
    search_fields = ('product', 'name')


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ('order', 'product', 'name', 'price', 'quantity')
    search_fields = ('order', 'product', 'name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'created_timestamp',
        'phone_number',
        'requires_delivery',
        'delivery_address',
        'payment_on_get',
        'is_paid',
        'status')

    list_display_links = ('user',)

    search_fields = (
        'id',
    )

    readonly_fields = (
        'created_timestamp',
    )

    list_filter = (
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
    )

    inlines = (OrderItemTabularAdmin,)


class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = (
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'created_timestamp',
    )

    search_fields = (
        'requires_delivery',
        'payment_on_get',
        'is_paid',
        'created_timestamp',
    )

    readonly_fields = ('created_timestamp',)
    extra = 0
