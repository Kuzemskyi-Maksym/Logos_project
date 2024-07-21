from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from main.models import Products
from carts.models import Cart

def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)
    
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    else:
        # Handle the case where HTTP_REFERER is not set
        return redirect('main:home')


def cart_remove(request, cart_id):

    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    else:
        # Handle the case where HTTP_REFERER is not set
        return redirect('accounts:users_cart')



def cart_change(request, cart_id, action):
    cart_item = get_object_or_404(Cart, id=cart_id)
    
    if action == 'increment':
        cart_item.quantity += 1
    elif action == 'decrement':
        cart_item.quantity = max(1, cart_item.quantity - 1)  # Запобігання зменшення кількості нижче 1
    
    cart_item.save()
    # return redirect('accounts:users_cart')  

    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    