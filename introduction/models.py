from django.db import models
from django.urls import reverse

class Category(models.Model):
    title=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True,allow_unicode=True)

    class Meta:
        ordering=['title']
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('introduction:show_introduction',args=[self.slug])

class Introduction(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='introductions')
    title=models.CharField(max_length=200,db_index=True)
    content=models.TextField()
    slug=models.SlugField(max_length=200,db_index=True,unique=True,allow_unicode=True)

    class Meta:
        ordering=['category']

    def __str__(self):
        return self.title
    
    