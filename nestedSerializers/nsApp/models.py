
from django.db import models

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=10)
    author = models.ForeignKey(Author, related_name='Books' ,on_delete=models.CASCADE)

