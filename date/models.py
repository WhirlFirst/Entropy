from django.db import models
from django.contrib.auth.models import User


class Date(models.Model):
    day = models.IntegerField()
    show= models.CharField(max_length=1000)

    def __str__(self):
        return self.show

class Processing(models.Model):
    name = models.CharField(max_length=50)
    iframe=models.CharField(max_length=100)
    Attribute=models.CharField(max_length=500)

    def __str__(self):
        return self.iframe