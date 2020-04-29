from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']
    prepopulated_fields={'slug':('title',)}

class IntroAdmin(admin.ModelAdmin):
    list_display=['title','category']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Introduction,IntroAdmin)
