from django.contrib import admin
from django.urls import path
from main import views


app_name = "main"


urlpatterns = [
    path('search/', views.index, name='search'),  # пошукова стрічка
    path('', views.index, name='home'), # головна сторінка
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'), # сторінка з деталями товару, по полю product_slug, яке автоматично генерується при створенні товару

]
