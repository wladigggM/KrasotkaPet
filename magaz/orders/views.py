from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from cart.utils import get_cart_user
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


# Create your views here.

class CreateOrderView(View):

    def get(self, request, *args, **kwargs):
        carts = get_cart_user(request)
        data = {
            'carts': carts,
            'form': CreateOrderForm(),
        }
        return render(request, 'create_order.html', data)

    def post(self, request, *args, **kwargs):
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = get_cart_user(request)

                    if not user.is_authenticated:
                        messages.error(request, 'Пользователь не аутентифицирован')
                        return redirect('login')  # Перенаправляем на страницу входа

                    if not cart_items.exists():
                        messages.error(request, 'Корзина пуста')
                        return redirect('cart')  # Перенаправляем на страницу корзины

                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data.get('phone_number'),
                        requires_delivery=form.cleaned_data.get('delivery_method'),
                        delivery_address=form.cleaned_data.get('address'),
                        payment_on_get=form.cleaned_data.get('payment_method'),
                    )

                    for cart_item in cart_items:
                        product = cart_item.product
                        name = product.name
                        price = product.sell_price()
                        quantity = cart_item.quantity
                        size = cart_item.size

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity,
                            size=size,
                        )

                    cart_items.delete()
                    messages.success(request, 'Заказ оформлен!')
                    return redirect(reverse('users:account'))  # Перенаправляем на страницу аккаунта
            except Exception as e:
                print(f'Error: {e}')
                messages.error(request, str(e))
        else:
            messages.error(request, 'Форма не валидна')

        data = {
            'form': form,
        }
        return render(request, 'create_order.html', data)

# def create_order(request):
#
#     return render(request, 'create_order.html')
