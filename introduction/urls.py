from django.urls import path
from .views import *

app_name = 'introduction'

urlpatterns = [
    path('', show_introduction, name='show_introduction'),
]