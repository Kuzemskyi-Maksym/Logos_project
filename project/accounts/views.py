from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import SignUpForm, UserLoginForm

def login(request):

    site_mobile_menu = True

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
        'site_mobile_menu': site_mobile_menu,
        'title': 'Login',
        'form': form,
    }
    return render(request, 'accounts/login.html', context)



def registration(request):

    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect('/accounts/profile')
    else:
        form = SignUpForm()

    site_mobile_menu = True


    context = {
        "site_mobile_menu": site_mobile_menu,
        'title': 'Registration',
        'form': form,

    }
    return render(request, 'accounts/registration.html', context)


def profile(request):
    context = {
        'title': 'Account'
    }
    return render(request, 'accounts/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/shop')


