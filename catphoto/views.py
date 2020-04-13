from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def show_catphoto(request):
    # 코딩합시다.

    return render(request, 'catphoto/photo.html',)