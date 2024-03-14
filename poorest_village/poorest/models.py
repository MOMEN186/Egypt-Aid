from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


USER_TYPE_CHOICES = (
     ('viewer', 'viewer'),
     ('admin', 'admin'))

RATING_CHOICES = (
    ('unknown', "unknown"),
    ('POOR','POOR'),
    ('GOOD','GOOD'),
    ('VERY GOOD','VERY GOOD'),
    ('EXCELLENT','EXCELLENT'))

SCHOOL_CHOICES = (
    ('unknown','unknown'),
    ('kinderkarten','kindergarten'),
    ('primary','primary'),
    ('secondary','secondary'),
    ('high','high'))

Infrastructure_CHOICES=(
    ("unknown","unknown"),
    ('electricity',"electricity"),
    ('sewer','sewer'),
    ('water','water'),
    ('gas','gas'),
    ('landline','landline'))

class User(AbstractUser):
    user_type=models.CharField(max_length=10,choices=USER_TYPE_CHOICES,default='viewer')

    def __str__(self):
        return f"{self.username}"
                                

class Government(models.Model):
    name=models.CharField(max_length=70)
    population=models.BigIntegerField(default=0)
    def __str__(self):
        return f"{self.name} {self.id} "
    

class Center(models.Model):
    name=models.CharField(max_length=64)
    government=models.ForeignKey(Government,on_delete=models.CASCADE)
    population=models.BigIntegerField(default=0)
    def __str__(self):
        return f"{self.name}"
    
    
class Village(models.Model):
    name=models.CharField(max_length=64)
    government=models.ForeignKey(Government,on_delete=models.CASCADE)
    center=models.ForeignKey(Center,on_delete=models.CASCADE)
    population=models.BigIntegerField(default=0)
    rating=models.CharField(max_length=10,choices=RATING_CHOICES,default="unknown")
    
    def __str__(self):
        return f"{self.name}{self.id}"
    

class School(models.Model):
    name=models.CharField(max_length=64)
    Gender=models.CharField(max_length=5)
    level=models.CharField(max_length=20,choices=SCHOOL_CHOICES)
    capacity=models.IntegerField(default=0)
    current_capacity=models.IntegerField(default=0)
    government=models.ForeignKey(Government,on_delete=models.CASCADE)
    center=models.ForeignKey(Center,on_delete=models.CASCADE)
    village=models.ForeignKey(Village,on_delete=models.CASCADE)
    
    def __str__(self):
     return f"{self.name} {self.id}"
 
 
class Medical(models.Model):
    name=models.CharField(max_length=64)
    government=models.ForeignKey(Government,on_delete=models.CASCADE)
    center=models.ForeignKey(Center,on_delete=models.CASCADE,blank=True,null=True)
    village=models.ForeignKey(Village,on_delete=models.CASCADE,blank=True,null=True)
    specialization=models.CharField(max_length=64)
    capacity=models.IntegerField(default=0)
    current_capacity=models.IntegerField(default=0)
    
         
class Holly_places(models.Model):
    name=models.CharField(max_length=64)
    government=models.ForeignKey(Government,on_delete=models.CASCADE)
    center=models.ForeignKey(Center,on_delete=models.CASCADE)
    village=models.ForeignKey(Village,on_delete=models.CASCADE)
    capacity=models.IntegerField(default=0)
    type=models.CharField(max_length=10,choices=(("mosque","mosque"),("church","church")),default="mosque")

class Infrastructure(models.Model):
    type=models.CharField(max_length=20,choices=Infrastructure_CHOICES,default="unknown")
    government=models.ForeignKey(Government,on_delete=models.CASCADE)
    center=models.ForeignKey(Center,on_delete=models.CASCADE)
    village=models.ForeignKey(Village,on_delete=models.CASCADE)
    capacity=models.IntegerField(default=0)



class public_safety(models.Model):
    type=models.CharField(max_length=64)
    government=models.ForeignKey(Government,on_delete=models.CASCADE)
    center=models.ForeignKey(Center,on_delete=models.CASCADE)
    village=models.ForeignKey(Village,on_delete=models.CASCADE,blank=True,default="",null=True)
    radius=models.IntegerField(default=0)

    
    