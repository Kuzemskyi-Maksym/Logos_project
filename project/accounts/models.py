from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Користувацька модель, яка розширює стандартну модель AbstractUser, додаючи додаткові поля для зображення та номера телефону.
    """
    image = models.ImageField(upload_to='user_images', blank=True, null=True, verbose_name='Avatar')

    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        """
        Мета-клас для налаштувань моделі. 
        Вказує назву таблиці в базі даних та задає відображення назви моделі в однині та множині.
        """
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

