# widgets.py

from django import forms
from django.utils.html import format_html
from django.templatetags.static import static

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
