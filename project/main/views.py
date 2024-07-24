from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from main.forms import CommentForm

from . import utils
from . import models
from . import choises

def index(request):
    products = models.Products.objects.all().order_by("id")

    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query_new = request.GET.get("q")

    if on_sale:
        products = products.filter(discount__gt=0)

    if order_by and order_by != "default":
        products = products.order_by(order_by)

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
    if query_new:
        products = utils.q_search(query_new)

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
        "query_params": query_params,
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

    comments = instance.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = instance
            new_comment.user = request.user
            new_comment.save()

            referer = request.META.get('HTTP_REFERER')
            if referer:
                return redirect(referer)
            else:
                # Handle the case where HTTP_REFERER is not set
                return redirect('main:home')
    else:
        comment_form = CommentForm()

    context = {
        "title": instance.name, 
        "object": instance, 
        'comments': comments,
        'comment_form': comment_form,
        }
    
    return render(request, "product_detail.html", context)
