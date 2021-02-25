from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<uuid:category_id>/', views.allProdCat, name='products_by_category'),
    path('product/<uuid:product_id>/', views.prod_detail,name = 'prod_detail'),
    path('product/create_new', views.prod_create,name='create_product'),
    path('product/<uuid:product_id>/edit', views.prod_update,name='edit_product'),
    path('product/<uuid:product_id>/delete', views.prod_delete,name='delete_product'),
    path('product/select_categories', views.prod_cat_select,name='cat_select'),
]