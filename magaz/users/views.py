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

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/sign_in.html'
    extra_context = {'title': 'Авторизация'}

    def form_valid(self, form):
        # Check if session_key exists
        session_key = self.request.session.session_key

        # Call the parent class method to complete the login process
        response = super().form_valid(form)
        # Set cookie with username
        username = self.request.user.username
        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=self.request.user)
        response.set_cookie('username', username, max_age=3600)
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
