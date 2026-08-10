from django.urls import path
from .import views
urlpatterns = [
    path('',views.recipe_list,name="recipe_list"),
    path('create/',views.create,name="recipe_create"),
    path('views_details/<int:id>',views.view_recipe,name="view_details"),
    path('update/<int:id>',views.recipe_update,name='update'),
    path('delete/<int:id>',views.recipe_delete,name='delete')
]
