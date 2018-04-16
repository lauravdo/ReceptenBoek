from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_category = models.CharField(max_length=200)
    recipe_url = models.URLField(max_length = 200)
    recipe_rating = models.IntegerFieldvalidators=([MinValueValidator(0), MaxValueValidator(10)])