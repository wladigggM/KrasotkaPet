from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, reverse_lazy
from . import views
from .views import AccountView

app_name = "users"
urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/', AccountView.as_view(), name='account'),
    path('register/', views.RegisterUser.as_view(success_url=reverse_lazy('users:login')), name='register'),

    path('password-reset/',
         PasswordResetView.as_view(template_name='users/password_reset.html',
                                   email_template_name='users/password_reset_email.html',
                                   success_url=reverse_lazy('users:password_reset_done')),
         name='password_reset'),

    path('password-reset-done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done',
         ),

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                          success_url=reverse_lazy('users:password_reset_complete')),
         name='password_reset_confirm'),

    path('password-reset/complete',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
