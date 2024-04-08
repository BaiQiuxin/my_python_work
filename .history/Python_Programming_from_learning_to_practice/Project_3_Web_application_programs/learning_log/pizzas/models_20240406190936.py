from django.db import models

# Create your models here.
class Pizza(models.Model):
    """创建一张pizza"""
    name = models.CharField()
    
    def __str__(self):
        """返回pizza名称"""
        return self.name

class Topping(models.Model):
    """披萨的顶料"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """返回配料的字符串表示"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text