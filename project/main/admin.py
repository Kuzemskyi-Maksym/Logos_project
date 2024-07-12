from django.contrib import admin
from main import models


@admin.register(models.Products)
class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}