from django.db import models

# Create your models here.
class Pizza(models.Model):
    """创建一张pizza"""
    name = models.CharField()
    
    def __str__(self):
        return self.name

class Topping(models.Model):
    """披萨的"""