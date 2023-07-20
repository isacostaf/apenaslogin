from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_or_create_account, name='login_or_create_account'),
    path('welcome/', views.welcome, name='welcome'),
]
