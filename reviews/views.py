from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.models import CustomUser
from .models import Review
import datetime

def add_review(request, prod_slug):
    product = get_object_or_404(Product, slug=prod_slug)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST or None, request.FILES)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            username = request.user.username
            image = form.cleaned_data['image']
            review = Review()
            review.product = product
            review.username = username
            review.rating = rating
            review.content = content
            review.title = title
            review.pub_date = datetime.datetime.now()
            review.image = image
            review.save()

            return HttpResponseRedirect(reverse('shop:prod_detail', kwargs={'prod_slug': prod_slug}))
    return render(request, 'add_review.html', {'product':product, 'form':form})

def review_update(request, prod_slug, id):
    product = get_object_or_404(Product, slug=prod_slug)
    review = get_object_or_404(Review, id=id)
    init_dict = {
        'rating':review.rating,
        'title':review.title,
        'content':review.content,
        'image':review.image
    }
    form = ReviewForm(request.POST or None, instance=review, initial=init_dict)
    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse('shop:prod_detail', kwargs={'prod_slug': prod_slug}))
    
    return render(request, 'update_review.html',{'form':form, 'product':product, 'review':review})

def review_delete(request, prod_slug, id):
    product = get_object_or_404(Product, slug=prod_slug)
    review = get_object_or_404(Review, id=id)
    if request.method == "POST":
        review.delete()

        return redirect("shop:allProdCat")
    
    return render(request, 'delete_review.html', {'product':product, 'review':review})