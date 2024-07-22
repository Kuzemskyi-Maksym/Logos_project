from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from carts.models import Cart

from .forms import SignUpForm, UserLoginForm, ProfileForm

def login(request):

    site_mobile_menu = True

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)

            # session_key = request.session.session_key

            if user is not None:
                auth.login(request, user)

                # if session_key:
                #     Cart.objects.filter(session_key = session_key).update(user=user)

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
    
    site_mobile_menu = True

    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                    Cart.objects.filter(session_key = session_key).update(user=user)

            if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
            return HttpResponseRedirect('/accounts/profile')
    else:
        form = SignUpForm()



    context = {
        "site_mobile_menu": site_mobile_menu,
        'title': 'Registration',
        'form': form,

    }
    return render(request, 'accounts/registration.html', context)


@login_required()
def logout(request):
    auth.logout(request)
    return redirect('/shop')


@login_required()
def profile(request):

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance = request.user, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile')
    else:
        form = ProfileForm(instance = request.user)

    context = {
        'title': 'Account',
        "form": form,
    }
    return render(request, 'accounts/profile.html', context)

def users_cart(request):

    site_mobile_menu = 'true'

    context = {
        "site_mobile_menu": site_mobile_menu,
        'title' : 'Users Cart',
    }

    return render(request, 'accounts/users_cart.html', context)
