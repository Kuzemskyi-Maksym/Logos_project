from django.contrib import admin
from main import models


@admin.register(models.Products)
class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ["name", "producer", "quantity", "price", "discount"]
    list_editable = ["quantity", "price", "discount"]
    search_fields = ['name', "producer"]
    list_filter = ['producer', 'discount', 'price']
    fields = [
        'image',
        'name',
        'description',
        'slug',
        ('producer', 'os'),
        ('price', 'discount'),
        'quantity',
        ('screen_diagonal', 'screen_coating', 'screen_resolution', 'touchscreen'),
        ('in_stock', 'is_new'),
        ('processor', 'number_of_processor_cores'),
        'ram',
        'ssd_scope',
        ('video_card_type', 'keyboard_backlighting'),
        ('additionally', 'color')

    ]
