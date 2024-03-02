from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from cart.utils import get_cart_user, add_to_cart
from mainApp.models import Item
from cart.models import Cart


# Create your views here.
class CartView(View):

    def get(self, request, *args, **kwargs):
        carts = get_cart_user(request)
        data = {
            'carts': carts,
        }
        return render(request, 'cart.html', data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1))
            product = Item.objects.get(id=product_id)
            user = request.user

            # Получите корзину текущего пользователя
            cart, created = Cart.objects.get_or_create(user=user, product=product)

            # Обновите количество товара в корзине
            if not created:
                cart.quantity += quantity
                cart.save()
            else:
                cart.quantity = quantity
                cart.save()

            # Возвращаем JSON-ответ с обновленным количеством товаров в корзине
            user_cart = Cart.objects.filter(user=user)
            user_cart_prod = user_cart.filter(product=product)

            cart_count = user_cart_prod.total_quantity()
            price_item = product.sell_price() * cart_count
            total_price = user_cart.total_price()

            return JsonResponse({'cartCount': cart_count,
                                 'priceItem': price_item,
                                 'totalPrice': total_price,
                                 })
        else:
            return JsonResponse({'error': 'Invalid request'}, status=400)


def cart_change(request, product_slug):
    ...


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
