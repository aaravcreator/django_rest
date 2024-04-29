from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recipe(models.Model):
    title=models.CharField(max_length=255)
    description = models.TextField()
    time_required = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=20,null=True)
    rating = models.FloatField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title