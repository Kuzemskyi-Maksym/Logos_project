from audioop import reverse
import email
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

from accounts.forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/accounts/profile')
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Login',
        'form': form
    }
    return render(request, 'accounts/login.html', context)



def registration(request):
    context = {
        'title': 'Registration'
    }
    return render(request, 'accounts/registration.html', context)


def profile(request):
    context = {
        'title': 'Account'
    }
    return render(request, 'accounts/profile.html', context)


def logout(request):
    ...


