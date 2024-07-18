from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "required": "",
        "name": "username",
        "id": "username",
        "type": "text",
        "class": "form-input w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
        "placeholder": "Username",
        "style": "height: 50px !important; margin-top: -20px !important;",
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "required": "",
        "name": "password",
        "id": "password",
        "type": "password",
        "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
        "placeholder": "Password",
        "style": "height: 50px !important; margin-top: 20px !important;",
        "maxlength": "22",
        "minlength": "8",
    }))

    class Meta:
        model = User
        fields = ['email', 'password']
