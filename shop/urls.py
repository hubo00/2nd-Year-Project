from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('shop/<slug:slug>/', views.allProdCat, name='products_by_category'),
    path('shop/product/<slug:slug>/', views.prod_detail,name = 'prod_detail'),
    path('shop/product/create_new', views.prod_create,name='create_product'),
    path('shop/product/<slug:slug>/edit', views.prod_update,name='edit_product'),
    path('shop/product/<slug:slug>/delete', views.prod_delete,name='delete_product'),
    path('shop/product/select_categories', views.prod_cat_select,name='cat_select'),
]