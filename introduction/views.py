from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def show_introduction(request,category_slug=None):
    current_category=None
    categories=Category.objects.all()
    introductions=Introduction.objects.all()

    if category_slug:
        current_category=get_object_or_404(Category,slug=category_slug)
        introductions=introductions.filter(category=current_category)

    return render(request, 'introduction/intro.html',{'current_category':current_category,'categories':categories,'introductions':introductions})