from django.urls import path

from . import views
from .models import Recipe

urlpatterns = [
    path('', views.index, name='index'),
    path('<recipe_name>/', views.name, name='name')
    # path('recipe_category/category', views.detail, name ='category')
]