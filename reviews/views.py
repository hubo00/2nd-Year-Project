from django.shortcuts import render, get_object_or_404
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
            content = form.cleaned_data['content']
            username = form.cleaned_data['username']
            image = form.cleaned_data['image']
            review = Review()
            review.product = product
            review.username = username
            review.rating = rating
            review.content = content
            review.pub_date = datetime.datetime.now()
            review.image = image
            review.save()

            return HttpResponseRedirect(reverse('shop:prod_detail', kwargs={'prod_slug': prod_slug}))
    return render(request, 'add_review.html', {'product':product, 'form':form})