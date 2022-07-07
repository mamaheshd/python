from django.db import models

# Create your models here.
class Laptops(models.Model):
    manufacturer=models.CharField(max_length=50,null=True,blank=True)
    name=models.CharField(max_length=20,null=True,blank=True)
    ram=models.CharField(max_length=20,null=True,blank=True)
    gpu=models.CharField(max_length=20,null=True,blank=True)
    cpu=models.CharField(max_length=20,null=True,blank=True)
    price=models.DecimalField(max_digits=50,null=True,decimal_places=2,blank=True)
    
    def __str__(self):
        return (self.name)