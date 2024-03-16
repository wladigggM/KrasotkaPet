from django.contrib import admin
from .models import *


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug_name')
    list_display_list = ('name', 'slug_name')
    readonly_fields = ('slug_name',)
    search_fields = ('name', 'slug_name')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at', 'updated_at',)
    filter_horizontal = ('size',)
    list_display_links = ('name',)
    readonly_fields = ('created_at', 'updated_at', 'slug_name', 'item_slug',)
    search_fields = ('name', 'id')
    fields = (
        'name', ('price', 'discount'), 'category', 'description', ('created_at', 'updated_at'),
        ('slug_name', 'item_slug'), 'size',)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'comment')
    list_display_list = ('name', 'email', 'rating', 'comment')
    search_fields = ('name', 'rating')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size_name',)


admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
