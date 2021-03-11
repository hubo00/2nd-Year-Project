from django.urls import path
from .import views

app_name = 'reviews'

urlpatterns = [
    path('<slug:prod_slug>/create_review', views.add_review, name='add_review'),
]