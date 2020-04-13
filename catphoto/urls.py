from django.urls import path
from .views import *

app_name = 'catphoto'

urlpatterns = [
    path('', show_catphoto, name='show_catphoto'),
]