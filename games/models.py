from django.db import models

# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Games(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre, related_name="genres")

    def __str__(self):
        return self.name
