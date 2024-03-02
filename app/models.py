from django.db import models

# Create your models here.
class student(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)





class user(models.Model):
    name =models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    phone=models.BigIntegerField(max_length=12)
    massage=models.CharField(max_length=200)

    


    