# Importing all the necessary Libraries and Utilities
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Product
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.models import CustomUser
from order.models import Order, OrderItem
from .models import Review
import datetime
from django.contrib import messages

"""
I used a course on Udemy to learn how to use machine learning in the django framework
A part of it showed how to create views for the review, I created the view myself, using pieces from the course, I created the update and delete views solely by myself.
-- Hubert Bukowski x00161897
source = https://www.udemy.com/course/machine-learning-projects-recommendation-system-website/
"""

# An add review function which displays a form for the user to fill out for their review
@login_required()
def add_review(request, prod_slug):
    email = str(request.user.email)
    orders = Order.objects.all().filter(emailAddress=email)
    product = get_object_or_404(Product, slug=prod_slug)
    form = ReviewForm()
    # If the request method is post, and all the form fields are valid, a new review object will be created
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
            review.user = request.user
            review.username = username
            review.rating = rating
            review.content = content
            review.title = title
            review.pub_date = datetime.datetime.now()
            review.image = image
            # Loops through each order for the user and checks if the product reviewed has been purchased
            for order in orders:
                # If the product HAS been purchased, set purchased (bool) field to true
                if OrderItem.objects.filter(order=order, product=product).exists():
                    review.purchased = True
            # Save the review, send a success message and redirect back to the product page
            review.save()
            messages.success(request, "Review Added Successfully")
            return HttpResponseRedirect(reverse('shop:prod_detail', kwargs={'prod_slug': prod_slug}))
    return render(request, 'add_review.html', {'product':product, 'form':form})

# A review update function which allows a user to update their existing reviews
@login_required()
def review_update(request, prod_slug, id):
    product = get_object_or_404(Product, slug=prod_slug)
    review = get_object_or_404(Review, id=id)
    email = str(request.user.email)
    orders = Order.objects.all().filter(emailAddress=email)
    # Dictionary containing initial field values for the form
    init_dict = {
        'rating':review.rating,
        'title':review.title,
        'content':review.content,
        'image':review.image
    }
    form = ReviewForm(request.POST or None, instance=review, initial=init_dict)
    # If all the form fields are entered successfully, save the form, send a success message and redirect to product page
    if form.is_valid():
        for order in orders:
                # If the product HAS been purchased, set purchased (bool) field to true
                if OrderItem.objects.filter(order=order, product=product).exists():
                    review.purchased = True
        form.save()
        messages.info(request, "Review Updated Successfully")
        return HttpResponseRedirect(reverse('shop:prod_detail', kwargs={'prod_slug': prod_slug}))
    
    return render(request, 'update_review.html',{'form':form, 'product':product, 'review':review})

# A review delete function which allows a user to delete their existing reviews
@login_required()
def review_delete(request, prod_slug, id):
    product = get_object_or_404(Product, slug=prod_slug)
    review = get_object_or_404(Review, id=id)
    if request.method == "POST":
        review.delete()
        messages.error(request, "Review Deleted Successfully")
        return redirect("shop:allProdCat")
    
    return render(request, 'delete_review.html', {'product':product, 'review':review})