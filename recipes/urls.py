from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_name', views.detail, name = 'detail')
    # path('recipe_category/category', views.detail, name ='category')
]