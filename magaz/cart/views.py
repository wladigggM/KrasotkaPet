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
        user = request.user
        if request.method == 'POST':
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1))
            cart_id = request.POST.get('cartId')
            action = request.POST.get('action')

            if action == 'delete':

                print('BLOCK FULL DEL')

                remove_cart = Cart.objects.get(id=cart_id)
                remove_cart.delete()
                user_cart = Cart.objects.filter(user=user)  # все телеги пользователя
                total_price = user_cart.total_price()
                total_quantity = user_cart.total_quantity()
                if user_cart.count() == 0:
                    total_user_carts = user_cart.count()
                    return JsonResponse({
                        'totalUserCart': total_user_carts,
                        'totalQuantity': total_quantity,
                        "totalPrice": total_price,
                        "success": True,
                        "message": "Корзина успешно удалена"
                    })

                return JsonResponse({
                    'totalQuantity': total_quantity,
                    "totalPrice": total_price,
                    "success": True,
                    "message": "Корзина успешно удалена"
                })
            elif action == 'increment':

                print('BLOCK INCREMENT')

                product = Item.objects.get(id=product_id)

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
                user_cart = Cart.objects.filter(user=user)  # все телеги пользователя
                user_cart_prod = user_cart.filter(product=product)  # телега с товаром

                cart_count = user_cart_prod.total_quantity()
                price_item = product.sell_price() * cart_count
                total_price = user_cart.total_price()
                total_quantity = user_cart.total_quantity()

                return JsonResponse({'cartCount': cart_count,
                                     'priceItem': price_item,
                                     'totalPrice': total_price,
                                     'totalQuantity': total_quantity,
                                     })
            elif action == 'decrement':

                print('BLOCK DECREMENT')

                product = Item.objects.get(id=product_id)

                cart = Cart.objects.get(user=user, product=product)

                print('QUANTITY', cart.quantity)
                print('CART_id', cart_id)

                cart.quantity += quantity
                cart.save()
                if cart.quantity == 0:

                    remove_cart = Cart.objects.get(id=cart_id)
                    remove_cart.delete()

                    user_cart = Cart.objects.filter(user=user)  # все телеги пользователя
                    total_price = user_cart.total_price()
                    total_quantity = user_cart.total_quantity()

                    if user_cart.count() == 0:
                        total_user_carts = user_cart.count()
                        return JsonResponse({
                            'totalUserCart': total_user_carts,
                            'totalQuantity': total_quantity,
                            "totalPrice": total_price,
                            "success": True,
                            "message": "Корзина успешно удалена"
                        })

                    user_cart = Cart.objects.filter(user=user)  # все телеги пользователя
                    total_price = user_cart.total_price()
                    total_quantity = user_cart.total_quantity()
                    return JsonResponse({
                        'totalQuantity': total_quantity,
                        "totalPrice": total_price,
                        "success": True,
                        "message": "Корзина успешно удалена"
                    })



                # Возвращаем JSON-ответ с обновленным количеством товаров в корзине
                user_cart = Cart.objects.filter(user=user)  # все телеги пользователя
                user_cart_prod = user_cart.filter(product=product)  # телега с товаром

                cart_count = user_cart_prod.total_quantity()
                price_item = product.sell_price() * cart_count
                total_price = user_cart.total_price()
                total_quantity = user_cart.total_quantity()

                return JsonResponse({'cartCount': cart_count,
                                     'priceItem': price_item,
                                     'totalPrice': total_price,
                                     'totalQuantity': total_quantity,
                                     })

                # if cart.quantity == 0:



        else:
            return JsonResponse({'error': 'Invalid request'}, status=400)
