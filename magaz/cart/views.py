from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from cart.utils import get_cart_user, ajax_request
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
        return ajax_request(request)
