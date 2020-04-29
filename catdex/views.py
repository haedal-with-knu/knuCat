from django.shortcuts import render, redirect,get_object_or_404
from .models import *

# Create your views here.
def show_catdex(request,subcategory_slug=None):
    current_category=None
    categories=Category.objects.all()
    subcategories=Subcategory.objects.all()
    cats=Cat.objects.all()

    if subcategory_slug:
        current_category=get_object_or_404(Subcategory,slug=subcategory_slug)
        cats=cats.filter(subcategory=current_category)
    return render(request, 'catdex/dex.html',{'current_category':current_category,'categories':categories,'cats':cats,'subcategories':subcategories})