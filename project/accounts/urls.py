from django.contrib import admin
from django.urls import path
from accounts import views


app_name = "accounts"


urlpatterns = [
    path('login/', views.login, name='login'), # вхід
    path('registration/', views.registration, name='registration'), # реєстрація
    path('profile/', views.profile, name='profile'), # профіль користувача
    path('users-cart/', views.users_cart, name='users_cart'), # корзина товарів
    path('logout/', views.logout, name='logout'), # вихід

]
