from . import models
from django.db.models import Q


def q_search(query_new):
    if query_new.isdigit() and len(query_new) <= 5:
        return models.Products.objects.filter(id = int(query_new))
    
    keywords = [word for word in query_new.split() if len(word) > 2]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(name__icontains=token) | Q(description__icontains=token)

    return models.Products.objects.filter(q_objects)
    
