from django.urls import path
from . import views  # Import the views module from the same directory

urlpatterns = [
    path('ingredient/add/', views.register_ingredient, name='register_ingredient'),
    path('ingredient/list/', views.ingredient_list, name='ingredient_list'),
]
