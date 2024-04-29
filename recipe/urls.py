from django.urls import path,include
from recipe import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'recipeviewset',views.RecipeViewSet,basename='recipeviewset')


urlpatterns = [
   path('hello/',views.hello),
   path('recipe_c/',views.RecipeListView.as_view()),
   path('recipe_c/<int:id>/',views.RecipeDetailView.as_view()),
   path('recipes/',views.list_recipe),
   path('recipes/<int:id>/',views.recipe_detail),
   path('api/',include(router.urls)),
]