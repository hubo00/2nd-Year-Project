# Importing utilities from django shortcuts. Importing category, product models
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, CatProd
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def allProdCat(request, category_id=None):
    c_page = None
    products_list = None
    if category_id != None:
        c_page = get_object_or_404(Category, id=category_id)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)

    '''Pagination code'''
    paginator = Paginator(products_list, 4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/category.html', {'category':c_page, 'products':products})

def prod_detail(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product':product})