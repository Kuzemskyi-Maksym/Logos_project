from django.contrib import admin

from carts import models

class CartTabAdmin(admin.TabularInline):
    model = models.Cart
    fields = 'product', 'quantity', 'created_timestump'
    search_fields = 'product', 'quantity', 'created_timestump'
    readonly_fields = ('created_timestump',) 
    extra = 1

    

@admin.register(models.Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ["user_display", "product_display", "quantity", "created_timestump"]
    list_filter = ['user', 'product__name', 'created_timestump']
    search_fields = ['user', ]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Anonymous'


    def product_display(self, obj):
        return str(obj.product.name)

