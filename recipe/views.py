from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response
from .models import Recipe,Category
from .serializers import RecipeSerializer,RecipeCreateSerializer,CategorySerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .pagination import LargeResultsSetPagination
# Create your views here.


# id = 1
# course = Course.objects.get(id=id)
# students_in_course = course.students.all()

class RecipeListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Recipe.objects.select_related('category','user').prefetch_related("ingredients")
    # queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # pagination_class = LargeResultsSetPagination



class CategoryView(APIView):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

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
            recipes = Recipe.objects.filter(title__icontains=title,user=request.user)
        else:
            recipes = Recipe.objects.filter(user=request.user)
        serializer = RecipeSerializer(recipes,many=True)
        return Response(serializer.data)

class RecipeDetailView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request,id,*args,**kwargs):
        # id = kwargs.get('id')
        print(id)
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response({
                'msg':'Recipe not found'
            },status=404)

        serializer = RecipeSerializer(recipe)
        # return Response(serializer.data)
        return Response(serializer.data)





@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])

def hello(request):
    return Response({
        'data':"Hello World"
    })



@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])

def who(request):
    user = request.user
    return Response({
        'user':user.username,
        'data':"Hello World"
    })





@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def list_recipe(request):
    if request.method == "POST":
        print(request.data)
        recipe_serializer = RecipeCreateSerializer(data=request.data)
        if recipe_serializer.is_valid(raise_exception=True):
            recipe_serializer.save(user=request.user)
            
            # recipe_serializer.save(user=request.user,time_required="30 mins",difficulty="EASY",rating=5)
            # validated_data = recipe_serializer.validated_data
            # recipe = Recipe(user=request.user,**validated_data)
            # recipe.save()
            # recipe_serializer = RecipeCreateSerializer(recipe)
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





@api_view()
def list_manual(request):
    recipes = Recipe.objects.all()

    data = [

    ]
    
    for recipe in recipes:

        recipe_object = {
            'id':recipe.id,
            'title_manual':recipe.title,
            'description':recipe.description,
            'time_required':recipe.time_required

        }
        print(recipe_object)
        data.append(
            recipe_object
        )
    print(data)
    response_data = {
        'recipes':data
    }
    return Response(response_data)


# Create your views here.
