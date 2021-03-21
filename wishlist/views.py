from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist, WishlistItem
from shop.models import Product
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

@login_required
def wishlist_detail(request):
    products = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
        products = WishlistItem.objects.filter(wishlist=wishlist)
    except ObjectDoesNotExist:
        wishlist = Wishlist.objects.create(user=request.user)
        wishlist.save()
    return render(request, 'wishlist_detail.html',{'wishlist':wishlist, 'products':products})

@login_required
def add_to_wishlist(request, prod_slug):
    product = get_object_or_404(Product, slug=prod_slug)
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except ObjectDoesNotExist:
        wishlist = Wishlist.objects.create(user=request.user)
        wishlist.save()

    all_wishlist_items = WishlistItem.objects.all().filter(wishlist=wishlist)

    try:
        wishlist_item = WishlistItem.objects.get(product=product, wishlist=wishlist)
    except ObjectDoesNotExist:
        wishlist_item = WishlistItem.objects.create(product=product, wishlist=wishlist)
        wishlist_item.save()
    return redirect('wishlist:wishlist_detail')

@login_required
def remove_from_wishlist(request, prod_slug):
    wishlist = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, slug=prod_slug)
    wishlist_item = WishlistItem.objects.get(product=product, wishlist=wishlist)
    wishlist_item.delete()
    return redirect('wishlist:wishlist_detail')