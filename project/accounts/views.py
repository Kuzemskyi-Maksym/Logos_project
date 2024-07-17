from django.shortcuts import render

def login(request):
    context = {
        'title': 'Login'
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


