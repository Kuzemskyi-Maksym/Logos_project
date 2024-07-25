# forms.py

from django import forms
from main.models import Comment
from .widgets import StarRatingWidget 


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