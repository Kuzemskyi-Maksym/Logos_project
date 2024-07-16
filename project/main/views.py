from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from . import models
from . import choises

# def index(request):
    # products = models.Products.objects.all().order_by("id")

    # selected_producers = request.GET.getlist('producers') 
    # selected_processors = request.GET.getlist('processors') 
    # selected_processor_cores = request.GET.getlist('processor_cores') 
    # selected_screen_coatings = request.GET.getlist('screen_coatings') 
    # selected_screen_diagonals = request.GET.getlist('screen_diagonals') 
    # selected_screen_resolutions = request.GET.getlist('screen_resolutions')
    # selected_rams = request.GET.getlist('rams')
    # selected_ssd_scopes = request.GET.getlist('ssd_scopes')
    # selected_oss = request.GET.getlist('oss')


    # # Використовуємо Q-об'єкти для створення фільтрів з логічним оператором OR
    # query = Q()
    # if selected_producers:
    #     query |= Q(producer__in=selected_producers)
    # if selected_processors:
    #     query |= Q(processor__in=selected_processors)
    # if selected_processor_cores:
    #     query |= Q(number_of_processor_cores__in=selected_processor_cores)
    # if selected_screen_coatings:
    #     query |= Q(screen_coating__in=selected_screen_coatings)
    # if selected_screen_diagonals:
    #     query |= Q(screen_diagonal__in=selected_screen_diagonals)
    # if selected_screen_resolutions:
    #     query |= Q(screen_resolution__in=selected_screen_resolutions)
    # if selected_rams:
    #     query |= Q(ram__in=selected_rams)
    # if selected_ssd_scopes:
    #     query |= Q(ssd_scope__in=selected_ssd_scopes)
    # if selected_oss:
    #     query |= Q(os__in=selected_oss)

    # # Якщо є умови для фільтрації, застосовуємо їх
    # if query:
    #     products = products.filter(query)

    # paginator = Paginator(products, 4)
    # page_request_variable = "page"
    # page = request.GET.get(page_request_variable, 1)
    # try:
    #     products = paginator.page(page)
    # except PageNotAnInteger:
    #     products = paginator.page(1)
    # except EmptyPage:
    #     products = paginator.page(1)

    # context = {
    #     "title": "Home",
    #     "products": products,
    #     "page_request_variable": page_request_variable,
    #     # 
    #     'selected_producers': selected_producers,
    #     'selected_processors': selected_processors,
    #     'selected_processor_cores': selected_processor_cores,
    #     'selected_screen_coatings': selected_screen_coatings,
    #     'selected_screen_diagonals': selected_screen_diagonals,
    #     'selected_screen_resolutions': selected_screen_resolutions,
    #     'selected_rams': selected_rams,
    #     'selected_ssd_scopes': selected_ssd_scopes,
    #     'selected_oss': selected_oss,
    #     #
    #     "producers": choises.PRODUCER,
    #     "processors": choises.PROCESSOR,
    #     "screen_coatings": choises.SCREEN_COATING,
    #     "screen_diagonals": choises.SCREEN_DIAGONAL,
    #     "screen_resolutions": choises.SCREEN_RESOLUTION,
    #     "rams": choises.RAM,
    #     "processor_cores": choises.PROCESSOR_CORES,
    #     "ssd_scopes": choises.SSD_SCOPE,
    #     "oss": choises.OS,
    #     "video_card_types": choises.VIDEO_CARD_TYPE,
    #     "colors": choises.COLOR,
    #     "additionallys": choises.ADDITIONALLY,
    # }
   
    # return render(request, "index.html", context)

def index(request):
    products = models.Products.objects.all().order_by("id")

    selected_producers = request.GET.getlist('producers') 
    selected_processors = request.GET.getlist('processors') 
    selected_processor_cores = request.GET.getlist('processor_cores') 
    selected_screen_coatings = request.GET.getlist('screen_coatings') 
    selected_screen_diagonals = request.GET.getlist('screen_diagonals') 
    selected_screen_resolutions = request.GET.getlist('screen_resolutions')
    selected_rams = request.GET.getlist('rams')
    selected_ssd_scopes = request.GET.getlist('ssd_scopes')
    selected_oss = request.GET.getlist('oss')


    # Використовуємо Q-об'єкти для створення фільтрів з логічним оператором OR
    query = Q()
    if selected_producers:
        query |= Q(producer__in=selected_producers)
    if selected_processors:
        query |= Q(processor__in=selected_processors)
    if selected_processor_cores:
        query |= Q(number_of_processor_cores__in=selected_processor_cores)
    if selected_screen_coatings:
        query |= Q(screen_coating__in=selected_screen_coatings)
    if selected_screen_diagonals:
        query |= Q(screen_diagonal__in=selected_screen_diagonals)
    if selected_screen_resolutions:
        query |= Q(screen_resolution__in=selected_screen_resolutions)
    if selected_rams:
        query |= Q(ram__in=selected_rams)
    if selected_ssd_scopes:
        query |= Q(ssd_scope__in=selected_ssd_scopes)
    if selected_oss:
        query |= Q(os__in=selected_oss)

    # Якщо є умови для фільтрації, застосовуємо їх
    if query:
        products = products.filter(query)

    paginator = Paginator(products, 4)
    page_request_variable = "page"
    page = request.GET.get(page_request_variable, 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(1)

    # Збереження параметрів фільтрації в URL
    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page')

    context = {
        "title": "Home",
        "products": products,
        "page_request_variable": page_request_variable,
        "query_params": query_params,  # Передаємо параметри в шаблон
        # 
        'selected_producers': selected_producers,
        'selected_processors': selected_processors,
        'selected_processor_cores': selected_processor_cores,
        'selected_screen_coatings': selected_screen_coatings,
        'selected_screen_diagonals': selected_screen_diagonals,
        'selected_screen_resolutions': selected_screen_resolutions,
        'selected_rams': selected_rams,
        'selected_ssd_scopes': selected_ssd_scopes,
        'selected_oss': selected_oss,
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
        "additionallys": choises.ADDITIONALLY,
    }
   
    return render(request, "index.html", context)



# def product_detail(request):
def product_detail(request, product_slug=None):
    instance = get_object_or_404(models.Products, slug=product_slug)
    context = {"title": instance.name, "object": instance}
    return render(request, "product_detail.html", context)
