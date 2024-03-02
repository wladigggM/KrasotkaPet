from django.http import JsonResponse

from cart.models import Cart
from mainApp.models import Item


def get_cart_user(request):
    carts = Cart.objects.none()

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
        print(carts)
    return carts


def add_to_cart(request):
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
        cart_count = user_cart.total_quantity()
        print(cart_count)
        return JsonResponse({'cartCount': cart_count})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)