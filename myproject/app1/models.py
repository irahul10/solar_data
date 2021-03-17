from django.db import models

# Create your models here.
# class student2(models.Model):
#     name = models.CharField(max_length=100)
#     branch=models.CharField(max_length=100)
#     email=models.EmailField(max_length=100, default='null')
#     def __str__(self): #python 2 def __unicode__(self):
#         return self.email

class Student(models.Model):
    name=models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Logindata(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)
    def __str__(self):
        return self.email


