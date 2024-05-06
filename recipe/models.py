from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images')

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
# Create your models here.
class Recipe(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,)
    ingredients = models.ManyToManyField(Ingredient,)
    title=models.CharField(max_length=255)
    description = models.TextField()
    time_required = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=20,null=True,blank=True)
    rating = models.FloatField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
    
