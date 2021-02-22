from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<uuid:category_id>/', views.allProdCat, name='products_by_category'),
    path('product/<uuid:product_id>/', views.prod_detail,name = 'prod_detail'),
    path('product/create_new', views.prod_create,name='create_product'),
]