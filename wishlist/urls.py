from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist_detail, name='wishlist_detail'),
    path('/add/<slug:prod_slug>', views.add_to_wishlist, name='add_to_wishlist'),
    path('/remove/<slug:prod_slug>', views.remove_from_wishlist, name='remove_from_wishlist'),
]