from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from mainApp.models import Item
from cart.models import Cart


# Create your views here.
class CartView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user)
            data = {
                'carts': carts,
            }
            return render(request, 'cart.html', data)

        return render(request, 'cart.html')


def cart_add(request, item_slug):
    product = Item.objects.get(item_slug=item_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    ...


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
