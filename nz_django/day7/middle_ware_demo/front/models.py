from django.db import models

class User(models.Model):
    telephone = models.CharField(max_length=11)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
