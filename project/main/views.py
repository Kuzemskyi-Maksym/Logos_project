from django.shortcuts import get_object_or_404, render
from . import models
from . import choises


def index(request):
    products = models.Products.objects.all().order_by('id')

    context = {
        "title": "Home",
        "products": products,
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
