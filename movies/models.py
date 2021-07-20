from django.db import models
from datetime import date

# Create your models here.

class Actor(models.Model):
    first_name    = models.CharField(max_length=20)
    last_name     = models.CharField(max_length=20)
    date_of_birth = models.DateTimeField()
    movies        = models.ManyToManyField('Movie', related_name='actors')

    class Meta:
        db_table = 'actors'
    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    running_time = models.IntegerField(default=0)

    class Meta:
        db_table = 'movies'
    
    def __str__(self):
        return self.title

