from django.contrib import auth
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from carts.models import Cart
from orders.models import Order, OrderItem

from .forms import SignUpForm, UserLoginForm, ProfileForm

"""
 **login(request)**: 
  - Опис: Обробляє вхід користувача.
  - Ціль: Аутентифікація користувача та перенаправлення на сторінку профілю у разі успіху.
  - Особливості: Використовує `UserLoginForm` для збору даних про користувача.

- **registration(request)**:
  - Опис: Обробляє реєстрацію нового користувача.
  - Ціль: Створення нового облікового запису, аутентифікація та перенаправлення на сторінку профілю.
  - Особливості: Використовує `SignUpForm` для збору даних про нового користувача.

- **logout(request)**:
  - Опис: Обробляє вихід користувача.
  - Ціль: Вихід користувача з системи та перенаправлення на сторінку магазину.
  - Особливості: Використовує декоратор `login_required` для захисту від неавторизованого доступу.

- **profile(request)**:
  - Опис: Відображає та редагує профіль користувача.
  - Ціль: Дозволяє користувачеві переглядати та оновлювати свої дані профілю та замовлення.
  - Особливості: Використовує `ProfileForm` для збору даних профілю, а також завантажує пов'язані замовлення користувача.

- **users_cart(request)**:
  - Опис: Відображає кошик користувача.
  - Ціль: Відображення товарів, доданих користувачем до кошика.
  - Особливості: Встановлює параметр `site_mobile_menu` для забезпечення мобільного меню на сторінці.
"""

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

    orders = (
        Order.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch(
                    'orderitem_set', 
                    queryset=OrderItem.objects.select_related('product'),
                )
            )
            .order_by("-id")
        
    )

    context = {
        'title': 'Account',
        "form": form,
        "orders": orders,
    }
    return render(request, 'accounts/profile.html', context)

def users_cart(request):

    site_mobile_menu = 'true'

    context = {
        "site_mobile_menu": site_mobile_menu,
        'title' : 'Users Cart',
    }

    return render(request, 'accounts/users_cart.html', context)
