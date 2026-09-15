from django.contrib import admin
from accounts import models
from carts.admin import CartTabAdmin

@admin.register(models.User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    search_fields = ["username", "first_name", "last_name", "email"]
    list_filter = ["username", "first_name", "last_name", "email"]

    inlines = [CartTabAdmin,]
