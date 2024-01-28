from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUser(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'login-form'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login-form'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Введите имя пользователя', widget=forms.TextInput())
    email = forms.CharField(label='Введите EMAIL', widget=forms.TextInput())
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']