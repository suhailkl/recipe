from django.shortcuts import render,redirect,get_object_or_404
from .models import Recipe
from .forms import RecipeForm
# Create your views here.
def recipe_list(request):
    recipes=Recipe.objects.all()
    return render(request,'recipe_list.html',{'recipes':recipes})

def create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form=RecipeForm()
    return render(request,'recipe_form.html',{'form':form})

def view_recipe(request,id):
    recipe=get_object_or_404(Recipe,id=id)
    return render(request,'recipe_view.html',{'recipe':recipe})

def recipe_update(request,id):
    recipe =get_object_or_404(Recipe,id=id)
    if request.method=='POST':
        form=RecipeForm(request.POST,request.FILES,instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request,'recipe_form.html',{'form':form})

def recipe_delete(request,id):
    recipe =get_object_or_404(Recipe,id=id)
    if request.method =='POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request,'delete.html',{'recipe':recipe})

