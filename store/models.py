from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)


    def __str__(self):
        return (self.name)

class Product(models.Model):
    product_id=models.AutoField(primary_key=True,default=1)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/images',default="")

    def _str_(self):
        return (self.name)-(self.product_id)-(self.description)
    
class Cart(models.Model):
    username=models.CharField(max_length=20,default='')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.username


  
class Customer(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=9)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
     
  
  
class Order(models.Model): 
    name = models.CharField(max_length=255)  # Ensure this field exists
    quantity = models.IntegerField(default=1) 
    address = models.CharField(max_length=255, default='', blank=True) 
    phone = models.CharField(max_length=50, default='', blank=True) 
    date = models.DateField(default=datetime.today) 
    status = models.BooleanField(default=False) 
  
    def __str__(self): 
          return f"{self.name}"
  
