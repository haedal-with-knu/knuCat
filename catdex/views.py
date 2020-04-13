from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def show_catdex(request):
    # 코딩합시다.

    return render(request, 'catdex/dex.html',)