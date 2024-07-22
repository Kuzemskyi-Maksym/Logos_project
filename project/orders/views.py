from django.shortcuts import render

def create_order(request):



    context = {
        'title': 'Create Order',
    }

    return render(request, 'orders/create_order.html', context)