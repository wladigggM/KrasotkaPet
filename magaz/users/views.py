from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.generic import CreateView

from users.forms import LoginUser, RegisterUserForm


# Create your views here.

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/sign_in.html'
    extra_context = {'title': 'Авторизация'}

@login_required(login_url='/users/login')
def account(request):
    return render(request, 'users/account.html')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'

