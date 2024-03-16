from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.views import View
from django.views.generic import CreateView, ListView

from cart.models import Cart
from cart.utils import ajax_request
from mainApp.models import Item
from users.forms import RegisterUserForm

# Create your views here.

from django.db.models import F


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/sign_in.html'
    extra_context = {'title': 'Авторизация'}

    def form_valid(self, form):
        session_key = self.request.session.session_key

        response = super().form_valid(form)

        current_user = self.request.user

        # Получить корзину текущего пользователя и предыдущую корзину с тем же session_key, если она есть
        current_cart = Cart.objects.filter(user=current_user)
        previous_cart = Cart.objects.filter(session_key=session_key)
        print(f'current_cart= {current_cart}'
              f'previous_cart = {previous_cart}')

        # Обновить количество товаров в текущей корзине, если они присутствуют в предыдущей корзине
        for item in previous_cart:
            matching_items = current_cart.filter(product=item.product, size=item.size)
            if matching_items.exists():
                matching_item = matching_items.first()
                matching_item.quantity = F('quantity') + item.quantity
                matching_item.save()
            else:
                item.user = current_user
                item.session_key = None
                item.save()

        previous_cart.delete()

        # Установить cookie с именем пользователя
        response.set_cookie('username', current_user.username, max_age=3600)

        return response


@login_required(login_url='/users/login')
def account(request):
    return render(request, 'users/account.html')


class AccountView(View):

    def get(self, request, *args, **kwargs):
        user_profile = self.request.user
        carts = Cart.objects.filter(user=user_profile)
        data = {
            'user': user_profile,
            'carts': carts,
        }
        return render(request, 'users/account.html', data)

    def post(self, request, *args, **kwargs):
        return ajax_request(request)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        session_key = self.request.session.session_key

        response = super().form_valid(form)

        if self.request.user.is_authenticated:
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=self.request.user)

        return response
