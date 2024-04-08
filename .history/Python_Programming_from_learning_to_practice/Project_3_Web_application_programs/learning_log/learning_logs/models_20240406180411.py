from django.db import models

class Topic(models,Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    da