from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe
# Create your views here.
class RecipeList(ListView):
  model = Recipe
  context_object_name = "recipe_list" 