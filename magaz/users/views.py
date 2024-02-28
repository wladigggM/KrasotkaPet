from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.generic import CreateView, ListView

from cart.models import Cart
from users.forms import LoginUser, RegisterUserForm


# Create your views here.

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/sign_in.html'
    extra_context = {'title': 'Авторизация'}

    def form_valid(self, form):
        r = super().form_valid(form)
        username = self.request.user.username
        r.set_cookie('username', username, max_age=3600)

        return r


@login_required(login_url='/users/login')
def account(request):
    return render(request, 'users/account.html')


class AccountView(ListView):

    def get(self, request, *args, **kwargs):
        user_profile = self.request.user
        carts = Cart.objects.filter(user=user_profile)
        data = {
            'user': user_profile,
            'carts': carts,
        }
        return render(request, 'users/account.html', data)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
