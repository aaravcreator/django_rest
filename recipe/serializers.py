from rest_framework import serializers
from .models import Recipe, Category,Ingredient


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["name",]

class RecipeSerializer(serializers.ModelSerializer):

    ingredients = IngredientSerializer(many=True)
    category = CategorySerializer()
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title','category','description','time_required','difficulty','rating','ingredients']