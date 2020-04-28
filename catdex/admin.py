from django.contrib import admin
from .models import *

#class CategoryAdmin(admin.ModelAdmin):
#    list_display=['name','slug']
#    prepopulated_fields={'slug':('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    prepopulated_fields={'slug':('name',)}

class SubcategoryAdmin(admin.ModelAdmin):
    list_display=['name','category']
    prepopulated_fields={'slug':('name',)}

class CatAdmim(admin.ModelAdmin):
    list_display=['name','slug','created']
    prepopulated_fields={'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)
admin.site.register(Cat,CatAdmim)