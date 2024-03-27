from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
