# forms.py

from django import forms
from main.models import Comment
from .widgets import StarRatingWidget

"""
### Імпортовані модулі та класи
- **forms**:
  - Опис: Модуль Django для створення форм.
  - Ціль: Використовується для створення форм на основі моделей та для роботи з різними полями форми.

- **Comment**:
  - Опис: Модель коментаря з основної програми.
  - Ціль: Використовується для визначення структури форми коментарів на основі цієї моделі.

- **StarRatingWidget**:
  - Опис: Кастомний віджет для зіркового рейтингу.
  - Ціль: Використовується для відображення та обробки зіркового рейтингу у формі.

### Класи
- **CommentForm**:
  - Опис: Форма для створення та редагування коментарів.
  - Ціль: Забезпечує зручний інтерфейс для введення тексту коментаря та зіркового рейтингу.
  - Властивості:
    - **Meta**: Внутрішній клас для налаштування метаданих форми.
      - **model**: Вказує на модель `Comment`, яка використовується для цієї форми.
      - **fields**: Поля форми, які мають бути відображені (`text` та `rating`).
      - **widgets**: Кастомні віджети для полів форми.
        - **text**: Використовує `forms.Textarea` з кастомними атрибутами для відображення текстового поля коментаря.
        - **rating**: Використовує `StarRatingWidget` для відображення зіркового рейтингу з вибором від 1 до 5 зірок.
"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={
                "required": "",
                'placeholder': 'Enter your comment here',
                "type": "text",
                "class": "form-control px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
                "style": "height: 170px !important; margin-top: 20px !important; width: 500px !important",
            }),
            'rating': StarRatingWidget(choices=[(i, f'{i} stars') for i in range(1, 6)]),
        }