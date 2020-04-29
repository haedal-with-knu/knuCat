from django.urls import path
from .views import *

app_name = 'catdex'

urlpatterns = [
    path('', show_catdex, name='show_catdex'),
    path('<subcategory_slug>/',show_catdex,name='show_catdex')
]