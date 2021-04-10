# Importing utilities from django shortcuts. Importing category, product models
from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect, redirect, reverse
from .models import Category, Product, subCategory
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .forms import ProductForm, ProductCreateForm
from reviews.models import Review
from wishlist.models import WishlistItem, Wishlist
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# An all product categories view which displays all the products, Specific category products,
# and specific subcategory products, depending on where a user is situated on the website
def allProdCat(request, cat_slug=None, subcat_slug=None):
    c_page = None
    products_list = None
    subcat = None
    # If the Category slug is not None, then retrieve all the products from all of the subcategories
    if cat_slug != None:
        c_page = get_object_or_404(Category, slug=cat_slug)
        subcat = get_list_or_404(subCategory, category=c_page)
        products_list = Product.objects.filter(category__in=subcat, available=True)
    # Otherwise if the Subcategory slug is not none, then retrieve all the products from that specific subcategory
    elif subcat_slug != None:
        subcat = get_object_or_404(subCategory, slug=subcat_slug)
        products_list = Product.objects.filter(category=subcat, available=True)
    # Else if the Category and subcategory slugs are both None, retrieve all of the currently 
    # available products site-wide
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

# A Product detail view which displays a specific product and Reviews that users have left
# on that product
def prod_detail(request, prod_slug):
    # Program will try to retrieve the product and reviews from the request, if not successful,
    # will raise Exception e
    try:
        product = Product.objects.get(slug=prod_slug)
        reviews = Review.objects.filter(product=product)
        inWishlist = False
    except Exception as e:
        raise e
    # If the user is currently logged in, then the program will attempt to retrieve the users wishlist
    if request.user.id:
        try:
            wishlist = Wishlist.objects.get(user=request.user)
        # If there is no wishlist related to the current user, program will create a new wishlist for that user
        except ObjectDoesNotExist:
            wishlist = Wishlist.objects.create(user=request.user)
            wishlist.save()
        # If the current product is already in the wishlist, set inWishlist value to True to signify occupancy in the wishlist
        if WishlistItem.objects.filter(wishlist=wishlist, product=product).exists():
            inWishlist = True

    return render(request, 'shop/product.html', {'product':product, 'reviews':reviews, 'in_wishlist': inWishlist})

# A product create view which allows an admin or member of staff create a new product
@login_required()
def prod_create(request):
    # Check if the requesting user is superuser or staff
    if request.user.is_superuser or request.user.is_staff:
        form = ProductCreateForm()
        # If the request method is post, save the product, display an appropriate message and redirect to the homepage
        if request.method=='POST':
            form = ProductForm(request.POST or None, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Product added successfully")
                return redirect("shop:allProdCat")
    # Else if the user is not admin or staff then return a HTTP forbidden Response
    else:
        return HttpResponseForbidden("User must be staff")
    return render(request, 'shop/create_view.html',{'form':form,'prod':Product.objects.all()})

# A product update vieww which allows an admin or member of staff to update an existing product
@login_required()
def prod_update(request, prod_slug):
    # Check if the requesting user is superuser or staff
    if request.user.is_superuser or request.user.is_staff:
        product = get_object_or_404(Product, slug=prod_slug)
        # Setting the initial form values to be the pre-existing product information
        init_dict = {
            'name':product.name,
            'name_alt':product.name_alt,
            'description':product.description,
            'price':product.price,
            'image':product.image,
            'stock':product.stock}
        form = ProductForm(request.POST or None, instance=product, initial=init_dict)
        # Save the form when all the values are correct
        if form.is_valid():
            form.save()
    # Else if the user is not admin or staff then return a HTTP forbidden Response
    else:
        return HttpResponseForbidden("User must be staff")
    return render(request, 'shop/update_view.html',{'form':form, 'product':product})

# A product delete view which allows an admin or member of staff to delete an existing product
@login_required()
def prod_delete(request, prod_slug):
    # Check if the requesting user is superuser or staff
    if request.user.is_superuser or request.user.is_staff:
        product = Product.objects.get(slug=prod_slug)
        # If the request method is POST, delete the product, display an appropriate message and redirect to homepage
        if request.method == "POST":
            product.delete()
            messages.error(request, "Product has been removed")
            return redirect("shop:allProdCat")
    # Else if the user is not admin or staff then return a HTTP forbidden Response
    else:
        return HttpResponseForbidden("User must be staff")

    return render(request, 'shop/delete_view.html',{'product':product})
