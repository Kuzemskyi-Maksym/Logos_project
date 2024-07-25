from . import models
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
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


def q_search(query_new):
    if query_new.isdigit() and len(query_new) <= 5:
        return models.Products.objects.filter(id = int(query_new))
    
    vector = SearchVector('name', 'description')
    query = SearchQuery(query_new)
    
    return models.Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')    
