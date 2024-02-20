from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ingredient/register/', views.register_ingredient, name='register_ingredient'),
]