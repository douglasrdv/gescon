from django.shortcuts import render, redirect
from .models import Ingredient

def register_ingredient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price_per_unit = request.POST.get('price_per_unit')
        quantity = request.POST.get('quantity')
        Ingredient.objects.create(name=name, price_per_unit=price_per_unit, quantity=quantity)
        return redirect('ingredient_list')  # Redirect to ingredient list view
    return render(request, 'gestor/ingredient_form.html')
