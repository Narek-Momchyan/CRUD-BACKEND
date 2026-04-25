from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
   
    fullName = models.CharField(max_length=255)

    facultet = models.CharField(max_length=100)

    age = models.IntegerField()
 
    phone = models.CharField(max_length=20)

    email = models.EmailField(unique=True)
  
    about = models.TextField()

    def __str__(self):
        return self.fullName
