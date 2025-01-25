from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.Model):
    name=models.CharField(max_length=200)

    def _str_(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def _str_(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

  
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
     
  
  
class Order(models.Model): 
    product = models.ForeignKey(User, 
            on_delete=models.CASCADE,default=1) 
    quantity = models.IntegerField(default=1) 
    address = models.CharField(max_length=255, default='', blank=True) 
    phone = models.CharField(max_length=50, default='', blank=True) 
    date = models.DateField(default=datetime.today) 
    status = models.BooleanField(default=False) 
  
    def __str__(self): 
          return self.product
  
