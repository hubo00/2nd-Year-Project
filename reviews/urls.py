from django.urls import path
from .import views

app_name = 'reviews'

urlpatterns = [
    path('<slug:prod_slug>/create_review', views.add_review, name='add_review'),
    path('<slug:prod_slug>/<int:id>/edit', views.review_update, name='edit_review'),
    path('<slug:prod_slug>/<int:id>/delete', views.review_delete, name='delete_review'),
]