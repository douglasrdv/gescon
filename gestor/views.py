from django.shortcuts import render, redirect
from .forms import IngredientForm
from .models import Ingredient

def register_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')  # assuming you have a URL named 'ingredient_list'
    else:
        form = IngredientForm()
    return render(request, 'ingredients/register_ingredient.html', {'form': form})


def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredients/ingredient_list.html', {'ingredients': ingredients})
