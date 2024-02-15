from django.db import models
import uuid
from django.conf import settings
from django import forms

# Create your models here.
class Movie(models.Model):
    uu_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to='movie_images/')
    image_cover = models.ImageField(upload_to='movie_images/')
    video = models.FileField(upload_to='movie_videos/')
    movie_views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class MovieList(models.Model):
    owner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class EmailModel(models.Model):
    email = models.EmailField(max_length=254)


class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.IntegerField()
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    