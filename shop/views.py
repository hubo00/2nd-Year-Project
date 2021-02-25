# Importing utilities from django shortcuts. Importing category, product models
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import Category, Product, CatProd
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .forms import ProductForm, CatProdForm

def allProdCat(request, category_id=None):
    c_page = None
    products_list = None
    if category_id != None:
        c_page = get_object_or_404(Category, id=category_id)
        products_list = Product.objects.filter(category=c_page, available=True)
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
    return render(request, 'shop/category.html', {'category':c_page, 'products':products})

def prod_detail(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product':product})

def prod_create(request):
    form = ProductForm()
    if request.method=='POST':
        form = ProductForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()

            return redirect("shop:cat_select")

    return render(request, 'shop/create_view.html',{'form':form,'prod':Product.objects.all()})

def prod_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
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

def prod_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        product.delete()

        return redirect("shop:allProdCat")

    return render(request, 'shop/delete_view.html',{'product':product})

def prod_cat_select(request):
    form = CatProdForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, 'shop/select_category.html',{'form':form})