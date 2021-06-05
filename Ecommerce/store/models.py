from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    contact=models.IntegerField()
    query=models.CharField(max_length=200)
     
    def __str__(self):
        return self.name


# Create your models here.

