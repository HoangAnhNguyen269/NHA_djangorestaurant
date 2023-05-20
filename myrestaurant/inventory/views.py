from django.shortcuts import render
#import Views
from django.views.generic import TemplateView
#import models
from .models import Ingredient, MenuItem, RecipeRequirements, Purchase


class HomeView(TemplateView):
    template_name = 'inventory/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.all()
        context['menu_items'] = MenuItem.objects.all()
        context['purchases'] = Purchase.objects.all()
        return context
    