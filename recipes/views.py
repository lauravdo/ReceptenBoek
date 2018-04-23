from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.template import loader

# Create your views here.

def index(request):
    sorted_recipe_list = Recipe.objects.order_by('recipe_name')[:5]
    template = loader.get_template('recipes/index.html')
    context = {
        'sorted_recipe_list': sorted_recipe_list,
    }

    return HttpResponse(template.render(context,request))

def name(request, recipe_name):
    response = "You're looking at recipe %s"
    return HttpResponse(response % recipe_name)

# def category(request, recipe_category)
#     response = "You're looking at category %s"
#     return HttpResponse(response % recipe_category)