from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.CharField(max_length=100, default='Uncategories')
    location = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.title + ' --- ' + str(self.author)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name