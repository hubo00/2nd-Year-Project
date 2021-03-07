from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('shop/<slug:cat_slug>/', views.allProdCat, name='products_by_category'),
    path('shop/subcategory/<slug:subcat_slug>/', views.allProdCat, name='products_by_subcategory'),
    path('shop/product/<slug:prod_slug>/', views.prod_detail,name = 'prod_detail'),
    path('shop/product/create_new', views.prod_create,name='create_product'),
    path('shop/product/<slug:prod_slug>/edit', views.prod_update,name='edit_product'),
    path('shop/product/<slug:prod_slug>/delete', views.prod_delete,name='delete_product'),
]