from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    ingredients=models.TextField()
    preparation = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='recipes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe_name