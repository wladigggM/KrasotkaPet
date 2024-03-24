from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cart.admin import CartTabular
from orders.admin import OrderTabularAdmin
from .models import User


# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'photo', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)

    inlines = (OrderTabularAdmin, CartTabular, )


admin.site.register(User, CustomUserAdmin)
