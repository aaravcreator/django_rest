from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class RecipeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        title = request.query_params.get('title')
        print(title)
        if title is not None:
            recipes = Recipe.objects.filter(title__icontains=title)
        else:
            recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes,many=True)
        return Response(serializer.data)

class RecipeDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        # id = self.kwargs.get('id')
        # print(id)
        # serializer = RecipeSerializer(recipes,many=True)
        # return Response(serializer.data)
        return Response({})





@api_view()
@permission_classes([IsAuthenticated])
def hello(request):
    return Response({
        'data':"Hello World"
    })


@api_view(['GET','POST'])
def list_recipe(request):
    if request.method == "POST":
        print(request.data)
        recipe_serializer = RecipeSerializer(data=request.data)
        if recipe_serializer.is_valid(raise_exception=True):
            recipe_serializer.save()
            return Response(recipe_serializer.data,status=201)
        else:
            print(recipe_serializer.errors)
            return Response(recipe_serializer.errors)
       
        
    else:
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes,many=True)
        response_data = serializer.data
        return Response(response_data)


@api_view(['GET','DELETE','PUT'])
def recipe_detail(request,id):

    try:
        recipe = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        return Response(data={"detail":"Requested recipe doesn't exist"},status=404)
    
    if request.method == "GET":
        # recipe = Recipe.objects.get(id=id)
        recipe_serializer = RecipeSerializer(recipe)
        return Response(recipe_serializer.data)
    
    elif request.method =="PUT":
        # recipe = Recipe.objects.get(id=id)
        recipe_serializer = RecipeSerializer(recipe,data=request.data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return Response(recipe_serializer.data)
        else:
            return Response(recipe_serializer.errors)

    elif request.method == "DELETE" :
        # recipe = Recipe.objects.get(id=id)
        recipe.delete()
        return Response(status=204)








    # data = [

    # ]
    
    # for recipe in recipes:
    #     recipe_object = {
    #         'id':recipe.id,
    #         'title':recipe.title,
    #         'description':recipe.description,
    #         'time_required':recipe.time_required

    #     }
    #     print(recipe_object)
    #     data.append(
    #         recipe_object
    #     )
    # print(data)
    # response_data = {
    #     'recipes':data
    # }
    # return Response(response_data)


# Create your views here.
