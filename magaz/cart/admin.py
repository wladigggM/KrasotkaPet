from django.contrib import admin

from cart.models import Cart

# Register your models here.

admin.site.register(Cart)


@admin.register
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'product',
        'quantity',
        'session_key',
        'created_timestamp',
        'new_params',
        'size',
    )

    list_display_links = ('user',)

    search_fields = (
        'id',
        'user',

    )

    readonly_fields = (
        'created_timestamp',
    )


class CartTabular(admin.TabularInline):

    model = Cart

    fields = (
        'user',
        'product',
        'quantity',
        'size',
    )

    search_fields = (
        'user',
        'product',
        'quantity',
        'size',
    )

    extra = 0
