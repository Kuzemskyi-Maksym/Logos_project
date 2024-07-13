from tabnanny import verbose
from django.db import models
from multiselectfield import MultiSelectField
from . import choises


class Products(models.Model):
    name = models.CharField(max_length=300, unique=False, blank=False, null=False)
    slug = models.SlugField(
        max_length=200, unique=True, blank=False, null=False, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="goods/images", blank=False, null=False)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    producer = models.CharField(choices=choises.PRODUCER, max_length=100, default=' ')
    screen_diagonal = models.CharField(choices=choises.SCREEN_DIAGONAL, max_length=40, default=' ')
    screen_coating = models.CharField(choices=choises.SCREEN_COATING, max_length=40, default=' ')
    in_stock = models.BooleanField(default=True)
    screen_resolution = models.CharField(
        choices=choises.SCREEN_RESOLUTION, max_length=40, default=' '
    )
    touchscreen = models.BooleanField(default=False)
    processor = models.CharField(choices=choises.PROCESSOR, max_length=60, default=' ')
    number_of_processor_cores = models.CharField(
        choices=choises.PROCESSOR_CORES, max_length=40, default=' '
    )
    ram = models.CharField(choices=choises.RAM, max_length=60, default=' ')
    ssd_scope = models.CharField(choices=choises.SSD_SCOPE, max_length=70, default=' ')
    video_card_type = models.CharField(choices=choises.VIDEO_CARD_TYPE, max_length=50, default=' ')
    keyboard_backlighting = models.BooleanField(default=True)
    os = models.CharField(choices=choises.OS, max_length=100, default=' ')
    additionally = MultiSelectField(choices=choises.ADDITIONALLY, default=' ')
    color = models.CharField(choices=choises.COLOR, max_length=100, default=' ')
    is_new = models.BooleanField(default=True)

    # def get_absolute_url(self) -> str:
    #     return f"/shop/product_detail/{self.id}"

    def __str__(self) -> str:
        return self.name
    
    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), 2)
        return self.price


    class Meta:
        db_table = "Product"
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
