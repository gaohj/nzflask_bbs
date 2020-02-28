from django.db import models
from django.core import validators

class Book(models.Model):
    b_name = models.CharField(max_length=30)
    b_price = models.FloatField(default=1.0)


class Game(models.Model):
    g_name = models.CharField(max_length=30)
    g_price = models.FloatField(default=1.0)


class Movie(models.Model):
    m_name = models.CharField(max_length=30)
    m_price = models.FloatField(default=1.0)


class User(models.Model):
    u_name = models.CharField(max_length=50,unique=True,validators=[validators.MinLengthValidator(6,message='最长50最短6位')])
    m_password = models.CharField(max_length=50,validators=[validators.MinLengthValidator(6,message='最长50最短6位')])