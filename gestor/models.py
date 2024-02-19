from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredient_id = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    yield_quantity = models.PositiveIntegerField(default=0)
    loss_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)


class RecipeIngredient(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2)


class Purchase(models.Model):
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)


class Client(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()


class Sale(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)


class CashFlow(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

 
class Stock(models.Model):
    ingredient_id = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    average_cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)