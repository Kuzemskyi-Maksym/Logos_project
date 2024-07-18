from . import models
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q


def q_search(query_new):
    if query_new.isdigit() and len(query_new) <= 5:
        return models.Products.objects.filter(id = int(query_new))
    
    vector = SearchVector('name', 'description')
    query = SearchQuery(query_new)
    
    return models.Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')    
