from django.shortcuts import render

from .models

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')