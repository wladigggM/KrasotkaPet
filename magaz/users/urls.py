from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/', views.account, name='account'),
    path('register/', views.RegisterUser.as_view()),
]