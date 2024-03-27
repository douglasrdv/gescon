from django.shortcuts import render, redirect
from django.db.models import Sum
from .forms import IngredientForm
from .models import Ingredient

def register_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'ingredients/register_ingredient.html', {'form': form})


def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    calculate_average_cost_per_product()
    return render(request, 'ingredients/ingredient_list.html', {'ingredients': ingredients})


def calculate_average_cost_per_product():
    ingredients = Ingredient.objects.values('name').annotate(
        total_value=Sum('cost' * ('quantity')),
        total_quantity=Sum('quantity')
    ).filter(total_quantity__gt=0)

    for ingredient in ingredients:
        average_cost = ingredient['total_value'] / ingredient['total_quantity']
        print(f'Average cost per unit of {ingredient["name"]}: ${average_cost:.2f}')
