from django.db import models

# Create your models here.
class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    Email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    


    