from django.contrib.auth.models import User
from django.http import JsonResponse

from cart.models import Cart
from mainApp.models import Item


def get_cart_user(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)

    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key)


def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = Item.objects.get(id=product_id)
        user = request.user
        if request.user.is_authenticated:
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
            return JsonResponse({'cartCount': cart_count})

        else:
            print('else')
            # Получите корзину текущего пользователя
            cart, created = Cart.objects.get_or_create(session_key=request.session.session_key, product=product)

            # Обновите количество товара в корзине
            if not created:
                cart.quantity += quantity
                cart.save()
            else:
                cart.quantity = quantity
                cart.save()

            # Возвращаем JSON-ответ с обновленным количеством товаров в корзине
            user_cart = Cart.objects.filter(session_key=request.session.session_key)
            cart_count = user_cart.total_quantity()
            print(cart_count)
            return JsonResponse({'cartCount': cart_count})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


def update_cart_and_response(user_or_session_key, product, quantity, action, cart_id=None):
    data = {}
    success = False

    if isinstance(user_or_session_key, User):
        user = user_or_session_key
        filter_params = {'user': user}
    else:
        session_key = user_or_session_key
        filter_params = {'session_key': session_key}

    if action == 'delete':
        try:
            remove_cart = Cart.objects.get(id=cart_id, **filter_params)
            remove_cart.delete()
            success = True
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif action == 'increment':
        try:
            cart, created = Cart.objects.get_or_create(**filter_params, product=product)
            cart.quantity += quantity if not created else quantity - cart.quantity
            cart.save()
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif action == 'decrement':
        try:
            cart = Cart.objects.get(**filter_params, product=product)
            cart.quantity -= 1
            cart.save()
            if cart.quantity <= 0:
                cart.delete()
                success = True
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    user_cart = Cart.objects.filter(**filter_params)
    user_cart_prod = user_cart.filter(product=product)

    cart_count = user_cart_prod.total_quantity() if user_cart_prod.exists() else 0

    if product is not None:
        price_item = product.sell_price() * cart_count
    else:
        price_item = None

    total_price = user_cart.total_price()
    total_quantity = user_cart.total_quantity()
    total_user_carts = user_cart.count()

    data.update({
        'cartCount': cart_count,
        'priceItem': price_item,
        'totalPrice': total_price,
        'totalQuantity': total_quantity,
        'success': success,
        'message': "Корзина успешно удалена",
        'totalUserCart': total_user_carts
    })
    return data


def ajax_request(request):
    if request.method == 'POST':

        if request.user.is_authenticated:
            user = request.user
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1))
            cart_id = request.POST.get('cartId')
            action = request.POST.get('action')

            if action == 'delete':
                # print('Delete1')
                return JsonResponse(update_cart_and_response(user, None, quantity, action, cart_id))

            try:
                product = Item.objects.get(id=product_id)

                if action == 'increment':
                    # print('Increment1')
                    return JsonResponse(update_cart_and_response(user, product, quantity, action))

                elif action == 'decrement':
                    # print('decrement1')
                    return JsonResponse(update_cart_and_response(user, product, quantity, action, cart_id))

                # Если действие не соответствует ожидаемым значениям
                else:
                    return JsonResponse({'error': 'Invalid action'}, status=400)

            except Item.DoesNotExist:
                return JsonResponse({'error': 'Invalid product id'}, status=400)

        else:
            session_k = request.session.session_key
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1))
            cart_id = request.POST.get('cartId')
            action = request.POST.get('action')

            if action == 'delete':
                # print('Delete1')
                return JsonResponse(update_cart_and_response(session_k, None, quantity, action, cart_id))

            try:
                product = Item.objects.get(id=product_id)

                if action == 'increment':
                    # print('Increment1')
                    return JsonResponse(update_cart_and_response(session_k, product, quantity, action))

                elif action == 'decrement':
                    # print('decrement1')
                    return JsonResponse(update_cart_and_response(session_k, product, quantity, action, cart_id))

                # Если действие не соответствует ожидаемым значениям
                else:
                    return JsonResponse({'error': 'Invalid action'}, status=400)

            except Item.DoesNotExist:
                return JsonResponse({'error': 'Invalid product id'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)
