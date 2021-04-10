from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist, WishlistItem
from shop.models import Product
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# A wishlist detail view which allows a user to browse their wishlist
@login_required()
def wishlist_detail(request, wishlist_counter=0):
    products = None
    # Tries to find the users wishlist and the associated products
    try:
        wishlist = Wishlist.objects.get(user=request.user)
        products = WishlistItem.objects.filter(wishlist=wishlist)
        # Counts each product currently stored in the wishlist
        for product in products:
            wishlist_counter += 1
    # If the user doesn't have a wishlist, A new one will be created for them
    except ObjectDoesNotExist:
        wishlist = Wishlist.objects.create(user=request.user)
        wishlist.save()
    return render(request, 'wishlist_detail.html',{'wishlist':wishlist, 'products':products, 'wishlist_counter': wishlist_counter})

# An add to wishlist function which allows a user to add a product into their wishlist
@login_required()
def add_to_wishlist(request, prod_slug):
    product = get_object_or_404(Product, slug=prod_slug)
    # Tries to search for the users wishlist
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    # If the user doesn't have a wishlist, a new one will be created for them
    except ObjectDoesNotExist:
        wishlist = Wishlist.objects.create(user=request.user)
        wishlist.save()
    # Checks to see if the desired product is already in the wishlist, if it is, it only redirects
    try:
        wishlist_item = WishlistItem.objects.get(product=product, wishlist=wishlist)
    # If the product isn't in the wishlist, then a new wishlist item is created and saved in the wishlist
    except ObjectDoesNotExist:
        wishlist_item = WishlistItem.objects.create(product=product, wishlist=wishlist)
        wishlist_item.save()
    # A success message is displayed and the user is redirected to their wishlist
    messages.success(request, "Product has been added to wishlist")
    return redirect('wishlist:wishlist_detail')

# A function to remove a product from the wishlist
@login_required()
def remove_from_wishlist(request, prod_slug):
    # Retrieves the wishlist and products associated with it
    wishlist = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, slug=prod_slug)
    wishlist_item = WishlistItem.objects.get(product=product, wishlist=wishlist)
    # Deletes the item, displays a message and refreshes the page
    wishlist_item.delete()
    messages.error(request, "Product has been removed from wishlist")
    return redirect('wishlist:wishlist_detail')

# A function to remove all products from the wishlist
@login_required()
def remove_all(request):
    # Retrieves the wishlist and all the products associated with it
    wishlist = Wishlist.objects.get(user=request.user)
    products = WishlistItem.objects.all().filter(wishlist=wishlist)
    # Deletes the products list, displays a message and refreshes the page
    products.delete()
    messages.error(request, "Wishlist has been Cleared")
    return redirect('wishlist:wishlist_detail')