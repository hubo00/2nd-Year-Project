from django.urls import path
from shop import views
from .views import signupView, signinView, signoutView, updateView, deleteView

urlpatterns = [
    path('create/', signupView, name='signup'),
    path('login/', signinView, name='signin'),
    path('logout/', signoutView, name='signout'),
    path('<int:pk>/update/', updateView.as_view(template_name='update.html'), name='account_update'),
    path('<int:pk>/delete/', deleteView.as_view(template_name='delete.html'), name='account_delete'),
]