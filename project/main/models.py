from tabnanny import verbose
from django.db import models
from django.forms import model_to_dict
from django.urls import reverse
from multiselectfield import MultiSelectField

from accounts.models import User
from . import choises

"""
### Імпортовані модулі та класи
- **verbose**:
  - Опис: Модуль для налаштування додаткових параметрів моделі.
  - Ціль: Забезпечує можливість налаштування більш детальних параметрів моделі.

- **models**:
  - Опис: Модуль Django для створення моделей бази даних.
  - Ціль: Використовується для визначення структур даних та їх взаємодії з базою даних.

- **model_to_dict**:
  - Опис: Функція для конвертації моделі у словник.
  - Ціль: Використовується для легкого перетворення моделей у словниковий формат.

- **reverse**:
  - Опис: Функція для створення URL-адрес за допомогою імені URL-шляху.
  - Ціль: Використовується для генерації URL-адрес у додатках Django.

- **MultiSelectField**:
  - Опис: Поле для зберігання декількох вибраних значень.
  - Ціль: Забезпечує можливість вибору декількох значень для одного поля.

### Моделі
- **Products**:
  - Опис: Модель для зберігання інформації про продукти (ноутбуки).
  - Ціль: Визначає структуру даних для продуктів у магазині.
  - Поля:
    - **name**: Назва продукту (тип: CharField).
    - **slug**: Унікальний URL-адрес (тип: SlugField).
    - **description**: Опис продукту (тип: TextField).
    - **image**: Зображення продукту (тип: ImageField).
    - **price**: Ціна продукту (тип: DecimalField).
    - **discount**: Знижка на продукт (тип: DecimalField).
    - **quantity**: Кількість продукту в наявності (тип: PositiveIntegerField).
    - **producer**: Виробник продукту (тип: CharField).
    - **screen_diagonal**: Діагональ екрану (тип: CharField).
    - **screen_coating**: Покриття екрану (тип: CharField).
    - **in_stock**: Наявність продукту на складі (тип: BooleanField).
    - **screen_resolution**: Роздільна здатність екрану (тип: CharField).
    - **touchscreen**: Підтримка сенсорного екрану (тип: BooleanField).
    - **processor**: Процесор (тип: CharField).
    - **number_of_processor_cores**: Кількість ядер процесора (тип: CharField).
    - **ram**: Обсяг оперативної пам'яті (тип: CharField).
    - **ssd_scope**: Обсяг SSD накопичувача (тип: CharField).
    - **video_card_type**: Тип відеокарти (тип: CharField).
    - **keyboard_backlighting**: Підсвітка клавіатури (тип: BooleanField).
    - **os**: Операційна система (тип: CharField).
    - **additionally**: Додаткові характеристики (тип: MultiSelectField).
    - **color**: Колір продукту (тип: CharField).
    - **is_new**: Показник новизни продукту (тип: BooleanField).
  - Методи:
    - **__str__**: Повертає назву продукту.
    - **get_absolute_url**: Повертає URL-адресу для перегляду детальної інформації про продукт.
    - **display_id**: Повертає відформатований ідентифікатор продукту.
    - **sell_price**: Повертає ціну з урахуванням знижки.
    - **average_rating**: Повертає середній рейтинг продукту.
  - Клас Meta:
    - **db_table**: Назва таблиці в базі даних.
    - **verbose_name**: Людинозрозуміла назва моделі.
    - **verbose_name_plural**: Людинозрозуміла назва моделі у множині.

- **Comment**:
  - Опис: Модель для зберігання коментарів до продуктів.
  - Ціль: Визначає структуру даних для коментарів користувачів.
  - Поля:
    - **product**: Зв'язок з моделлю продукту (тип: ForeignKey).
    - **user**: Зв'язок з моделлю користувача (тип: ForeignKey).
    - **text**: Текст коментаря (тип: TextField).
    - **rating**: Рейтинг продукту (тип: PositiveIntegerField).
    - **created_timestamp**: Час створення коментаря (тип: DateTimeField).
  - Методи:
    - **__str__**: Повертає текстовий опис коментаря.
  - Клас Meta:
    - **db_table**: Назва таблиці в базі даних.
    - **verbose_name**: Людинозрозуміла назва моделі.
    - **verbose_name_plural**: Людинозрозуміла назва моделі у множині.
"""


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
    

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("main:product_detail", kwargs={"product_slug": self.slug})
    
    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), 2)
        return self.price
    
    def average_rating(self):
        avg_rating = self.comments.aggregate(models.Avg('rating'))['rating__avg']
        return avg_rating or 0  # повертає середній рейтинг, або 0, якщо немає рейтингів
    
    
    class Meta:
        db_table = "Product"
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Comment(models.Model):
    product = models.ForeignKey(to=Products, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.name}'
    
    class Meta:
        db_table = "comment"
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'