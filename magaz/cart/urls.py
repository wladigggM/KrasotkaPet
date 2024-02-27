from django.urls import path
from cart.views import cart_add, cart_change, cart_remove, CartView

app_name = "cart"

urlpatterns = [
    path('cart_add/<slug:item_slug>/', cart_add, name='cart_add'),
    path('cart_change/<slug:item_slug>/', cart_change, name='cart_change'),
    path('cart_remove/<slug:item_slug>/', cart_remove, name='cart_remove'),
    path('cart/', CartView.as_view(), name='cart')
]