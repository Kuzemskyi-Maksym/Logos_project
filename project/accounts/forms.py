from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User


# Призначення: спеціальна форма реєстрації користувача для створення нового користувача 
# з додатковими полями та спеціальним стилем для кожного введення.
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "required": "",
                "name": "username",
                "id": "username",
                "type": "text",
                "class": "form-input w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
                "placeholder": "Username",
                "style": "height: 50px !important; margin-top: 20px !important;",
            }
        ),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "required": "",
                "name": "first_name",
                "id": "first_name",
                "type": "text",
                "class": "form-input w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
                "placeholder": "First Name",
                "style": "height: 50px !important; margin-top: 20px !important;",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "required": "",
                "name": "last_name",
                "id": "last_name",
                "type": "text",
                "class": "form-input w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
                "placeholder": "Last Name",
                "style": "height: 50px !important; margin-top: 20px !important;",
            }
        )
    )

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "required": "",
                "name": "email",
                "id": "email",
                "type": "email",
                "class": "form-input w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "placeholder": "Email",
                "style": "height: 50px !important;",
            }
        ),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "required": "",
                "name": "password",
                "id": "password1",
                "type": "password",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
                "placeholder": "Password",
                "style": "height: 50px !important; margin-top: 20px !important;",
                "maxlength": "22",
                "minlength": "8",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "required": "",
                "name": "password2",
                "id": "password2",
                "type": "password",
                "class": "form-input w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "placeholder": "Re-enter your password",
                "style": "height: 50px !important; margin-top: 20px !important;",
                "maxlength": "22",
                "minlength": "8",
            }
        )
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


# спеціальна форма входу користувача
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "required": "",
                "name": "username",
                "id": "username",
                "type": "text",
                "class": "form-input w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "placeholder": "Username",
                "style": "height: 50px !important; margin-top: -20px !important;",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "required": "",
                "name": "password",
                "id": "password",
                "type": "password",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
                "placeholder": "Password",
                "style": "height: 50px !important; margin-top: 20px !important;",
                "maxlength": "22",
                "minlength": "8",
            }
        )
    )

    class Meta:
        model = User
        fields = ["email", "password"]


# Custom профіль користувача
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",)

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
