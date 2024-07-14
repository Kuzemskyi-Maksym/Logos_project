from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from . import models
from . import choises


# def index(request):
#     selected_producers = request.GET.getlist('producers')  # Get selected producers as a list
#     products = models.Products.objects.all().order_by("id")

#     if selected_producers:
#         products = products.filter(producer__in=selected_producers)


#     paginator = Paginator(products, 40)
#     page_request_variable = "page"
#     page = request.GET.get(page_request_variable, 1)
#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         products = paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(1)

#     context = {
#         "title": "Home",
#         "products": products,
#         "page_request_variable": page_request_variable,
#         # 
#         "producers": choises.PRODUCER,
#         "processors": choises.PROCESSOR,
#         "screen_coatings": choises.SCREEN_COATING,
#         "screen_diagonals": choises.SCREEN_DIAGONAL,
#         "screen_resolutions": choises.SCREEN_RESOLUTION,
#         "rams": choises.RAM,
#         "processor_cores": choises.PROCESSOR_CORES,
#         "ssd_scopes": choises.SSD_SCOPE,
#         "oss": choises.OS,
#         "video_card_types": choises.VIDEO_CARD_TYPE,
#         "colors": choises.COLOR,
#         "additionallyes": choises.ADDITIONALLY,
#         #
#     }
    

#     return render(request, "index.html", context)

def index(request):
    products = models.Products.objects.all().order_by("id")

    selected_producers = request.GET.getlist('producers') # Отримати вибраних виробників у вигляді списку
    selected_processors = request.GET.getlist('processors') # Отримати вибраних виробників у вигляді списку


    if selected_producers:
        products = products.filter(producer__in=selected_producers)
    if selected_processors:
        products = products.filter(processor__in=selected_processors)

    paginator = Paginator(products, 40)
    page_request_variable = "page"
    page = request.GET.get(page_request_variable, 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(1)

    context = {
        "title": "Додому",
        "products": products,
        "page_request_variable": page_request_variable,
        'selected_producers': selected_producers,
        'selected_processors': selected_processors,
        #
        "producers": choises.PRODUCER,
        "processors": choises.PROCESSOR,
        "screen_coatings": choises.SCREEN_COATING,
        "screen_diagonals": choises.SCREEN_DIAGONAL,
        "screen_resolutions": choises.SCREEN_RESOLUTION,
        "rams": choises.RAM,
        "processor_cores": choises.PROCESSOR_CORES,
        "ssd_scopes": choises.SSD_SCOPE,
        "oss": choises.OS,
        "video_card_types": choises.VIDEO_CARD_TYPE,
        "colors": choises.COLOR,
        "additionallyes": choises.ADDITIONALLY,
    }
   
    return render(request, "index.html", context)





def about(request):
    context = {
        "title": "About us",
    }

    return render(request, "about_us.html", context)


# def product_detail(request):
def product_detail(request, product_slug=None):
    instance = get_object_or_404(models.Products, slug=product_slug)
    context = {"title": instance.name, "object": instance}
    return render(request, "product_detail.html", context)
