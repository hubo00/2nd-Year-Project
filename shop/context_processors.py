from django.shortcuts import get_list_or_404
from .models import Category, subCategory

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)