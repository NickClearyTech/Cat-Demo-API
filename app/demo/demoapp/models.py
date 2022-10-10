from email.policy import default
from random import choices
from secrets import choice
from django.db import models

# Create your models here.


class Cat(models.Model):
    class Meta:
        ordering = ['id']
    name = models.CharField(null=False, max_length=64)
    breed = models.CharField(null=False, max_length=32)
    age = models.IntegerField(null=False)
    sex = models.CharField(null=False, max_length=8, choices=[("Male", "Male"), ("Female", "Female")], default="Male")
    weight = models.IntegerField(null=False, default=5)
    adopted = models.BooleanField(null=False, default=True)


class Dog(models.Model):
    class Meta:
        ordering = ['id']
    name = models.CharField(null=False, max_length=64)
    breed = models.CharField(null=False, max_length=32)
    age = models.IntegerField(null=False)
