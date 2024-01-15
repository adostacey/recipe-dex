from django import forms

class RecipeForm(forms):
  name = forms.TextInput(help_text="Name of the recipe.")