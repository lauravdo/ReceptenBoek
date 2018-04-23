from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


# def validate_number(value):
#     if recipe_rating < 0 | recipe_rating > 10:
#         raise ValidationError('%s Number too small/big' % value)

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_category = models.CharField(max_length=200)
    recipe_url = models.URLField(max_length = 200)
    recipe_rating = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])
    def __str__(self):
        return self.recipe_name
    