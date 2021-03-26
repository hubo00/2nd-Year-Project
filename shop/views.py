# Importing utilities from django shortcuts. Importing category, product models
from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect, redirect, reverse
from .models import Category, Product, subCategory
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .forms import ProductForm
from reviews.models import Review
from django.contrib import messages

def allProdCat(request, cat_slug=None, subcat_slug=None):
    c_page = None
    products_list = None
    subcat = None
    if cat_slug != None:
        c_page = get_object_or_404(Category, slug=cat_slug)
        subcat = get_list_or_404(subCategory, category=c_page)
        products_list = Product.objects.filter(category__in=subcat, available=True)
    elif subcat_slug != None:
        subcat = get_object_or_404(subCategory, slug=subcat_slug)
        products_list = Product.objects.filter(category=subcat, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)

    '''Pagination code'''
    paginator = Paginator(products_list, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/category.html', {'category':c_page,'subcategory':subcat, 'products':products})

def prod_detail(request, prod_slug):
    average = 0
    try:
        product = Product.objects.get(slug=prod_slug)
        reviews = Review.objects.filter(product=product)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product':product, 'reviews':reviews})

def prod_create(request):
    form = ProductForm()
    if request.method=='POST':
        form = ProductForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully")
            return redirect("shop:allProdCat")

    return render(request, 'shop/create_view.html',{'form':form,'prod':Product.objects.all()})

def prod_update(request, prod_slug):
    product = get_object_or_404(Product, slug=prod_slug)
    init_dict = {
        'name':product.name,
        'name_alt':product.name_alt,
        'description':product.description,
        'price':product.price,
        'image':product.image,
        'stock':product.stock}
    form = ProductForm(request.POST or None, instance=product, initial=init_dict)
    if form.is_valid():
        form.save()
    return render(request, 'shop/update_view.html',{'form':form, 'product':product})

def prod_delete(request, prod_slug):
    product = Product.objects.get(slug=prod_slug)
    if request.method == "POST":
        product.delete()

        return redirect("shop:allProdCat")

    return render(request, 'shop/delete_view.html',{'product':product})
