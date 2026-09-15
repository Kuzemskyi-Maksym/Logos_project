from .models import Products

from . import models
# from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q

"""
### Імпортовані модулі та класи
- **models**:
  - Опис: Імпорт моделей з поточного додатку.
  - Ціль: Використовується для взаємодії з моделями бази даних.

- **SearchVector, SearchQuery, SearchRank**:
  - Опис: Класи з модуля `django.contrib.postgres.search`.
  - Ціль: Забезпечують функціональність повнотекстового пошуку у PostgreSQL.

- **Q**:
  - Опис: Клас для створення складних запитів до бази даних.
  - Ціль: Використовується для створення логічних умов у запитах.

### Функції
- **q_search(query_new)**:
  - Опис: Функція для пошуку продуктів за введеним запитом.
  - Ціль: Виконує пошук продуктів за ID або за назвою та описом за допомогою повнотекстового пошуку.
  - Аргументи:
    - **query_new**: Пошуковий запит від користувача (тип: str).
  - Логіка:
    - Якщо запит складається тільки з цифр і має довжину не більше 5 символів, виконується пошук продукту за ID.
    - Інакше виконується повнотекстовий пошук за назвою та описом продукту, результати сортуються за релевантністю.
"""


def q_search(query):
    # Якщо запит чисто числовий (id товару)
    if query.isdigit():
        return Products.objects.filter(id=int(query))

    # Звичайний пошук для SQLite через Q-об'єкти
    keywords = [word for word in query.split() if len(word) > 2]
    q_objects = Q()

    for token in keywords:
        q_objects |= Q(name__icontains=token)
        q_objects |= Q(description__icontains=token)

    return Products.objects.filter(q_objects)