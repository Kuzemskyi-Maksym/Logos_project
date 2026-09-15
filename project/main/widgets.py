# widgets.py

from django import forms
from django.utils.html import format_html
from django.templatetags.static import static

"""
### `StarRatingWidget` Клас

#### Імпортовані модулі
- **forms**: Імпорт класу `RadioSelect` з `django.forms` для створення радіо-кнопок.
- **format_html**: Функція для створення HTML-коду з форматом.
- **static**: Функція для отримання URL статичних файлів.

#### Методи

- **`__init__`**:
  - Опис: Ініціалізує віджет, викликаючи конструктор батьківського класу `RadioSelect`.
  - Аргументи:
    - `*args`, `**kwargs`: Передаються батьківському конструктору для забезпечення налаштувань віджету.

- **`get_context`**:
  - Опис: Перевизначає метод `get_context`, щоб налаштувати HTML-контекст для віджету.
  - Аргументи:
    - `name`: Ім'я віджету.
    - `value`: Значення, яке вибрано за замовчуванням.
    - `attrs`: Атрибути для віджету.
  - Логіка:
    - Отримує базовий контекст з `super().get_context()`.
    - Для кожної опції в контексті генерує HTML-код для зірок, використовуючи зображення зірки.
    - Оновлює мітки опцій (label) в контексті на основі зіркових зображень.
  - Повертає модифікований контекст, що включає HTML для відображення зірок.

### Пояснення

Цей віджет перетворює радіо-кнопки на візуально привабливі зіркові рейтинги. Замість стандартних кнопок віджет генерує HTML-код для зірок, які відображаються відповідно до вибраного значення рейтингу.

### Приклад використання

Якщо у вас є форма з полем рейтингу, ви можете використовувати цей віджет для відображення рейтингів у вигляді зірок:

```python
class MyForm(forms.Form):
    rating = forms.ChoiceField(choices=[(i, f'{i} stars') for i in range(1, 6)],
                               widget=StarRatingWidget())
```

У цьому випадку поле `rating` буде відображено як зірки, де вибране значення буде відображено відповідною кількістю зірок.
"""

class StarRatingWidget(forms.RadioSelect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        for widget in context['widget']['optgroups']:
            for option in widget[1]:
                option_value = int(option['value'])
                stars_html = format_html(
                    ''.join(
                        [format_html('<img src="{}" alt="star rating {}" class="star-rating">', static('images/star.svg'), i + 1) for i in range(option_value)]
                    )
                )
                option['label'] = stars_html
        return context
