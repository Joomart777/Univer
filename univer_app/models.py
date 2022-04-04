# from django.contrib.auth import get_user_model
from django.db import models



# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=30, primary_key=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.slug

class Univer (models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField()

    category = models.ForeignKey(Category, related_name='univer', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name