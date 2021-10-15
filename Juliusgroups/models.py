from django.db import models
from django.db.models.base import Model
from django.http import request



# Create your models here.

class login_Detials(models.Model):
    Username = models.CharField(max_length= 100)
    Password = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.Username
    
class Register_Account(models.Model):
    user = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_pass = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.fistname
    
class Contact_Forms(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email  = models.CharField(max_length=500)
    phone  = models.CharField(max_length=12)
    address = models.CharField(max_length=500)
    message  = models.TextField()

    
    def __str__(self):
        return self.Name
    
    
# class secondContactForm(models.Model):
#     fullname = models.CharField(max_length= 100)
#     email = models.EmailField()
#     contact = models.CharField(max_length=50)
#     message = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.fullname