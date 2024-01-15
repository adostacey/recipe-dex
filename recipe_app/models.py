from django.db import models

# Create your models here.


class Recipe(models.Model):
    choices_difficulty = [
        ("e", "Quick & Easy"),
        ("m", "Some Prep"),
        ("h", "Lots of prep or cook time."),
    ]

    choices_rating = [
        ("1", "Yum!"),
        ("2", "Om nom nom!!"),
        ("3", "Regrets!!!")
    ]

    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50, choices=choices_difficulty)
    directions = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_editted = models.DateField(auto_now=True)
    reference_url = models.URLField(blank=False)
    rating = models.CharField(max_length=50, choices=choices_rating)
    
    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class MeasuredIngredient(models.Model):
    choices_unit = [
        ("tsp", "tsp."),
        ("tbsp", "tbsp."),
        ("cup", "cup"),
        ("can", "can"),
        ("oz", "oz."),
        ("lb", "lb."),
    ]

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ManyToManyField(Ingredient)
    measurement = models.CharField(max_length=5)
    unit = models.CharField(max_length=50, choices=choices_unit)

    def __str__(self) -> str:
        return self.ingredient.first().name
