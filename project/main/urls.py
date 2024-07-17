from django.contrib import admin
from django.urls import path
from main import views


app_name = "main"


urlpatterns = [
    path('search/', views.index, name='search'),
    path('', views.index, name='home'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),

]
