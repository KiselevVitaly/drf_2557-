from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author:

    def __init__(self, name, birthday_year):
        self.name = name
        self.birthday_year = birthday_year

    def __str__(self):
        return self.name
    
class Biography:
    def __init__(self, text, author):
        self.author = author
        self.text = text

class Book:

    def __init__(self, name, authors):
        self.name = name
        self.authors = authors

class Article:

    def __init__(self, name, author):
        self.name = name
        self.author = author

from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField()

def __str__(self):
    return self.name
    

