from django.db import models

# Create your models here.
class Owner(models.Model):
    name  = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    age   = models.IntegerField(default=0)

    class Meta:
        db_table = 'owners'
    
    def __str__(self):
        return self.name

class Dog(models.Model):
    name  = models.CharField(max_length=20)
    age   = models.IntegerField(default=0)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, default='')

    class Meta:
        db_table = 'dogs'
    
    def __str__(self):
        return self.name

