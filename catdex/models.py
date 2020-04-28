from django.db import models
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True,allow_unicode=True)
    
    class Meta:
        ordering=['name']
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name
    
    #def get_absolute_url(self):
    #    return reverse('catdex:show_catdex',args=[self.slug])

class Subcategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name='subcategories')
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True,allow_unicode=True)
    class Meta:
        ordering=['category','name']
        verbose_name='subcategory'
        verbose_name_plural='subcategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catdex:show_catdex',args=[self.slug])

class Cat(models.Model):
    
    DOMAIN=(
        ('쪽문','쪽문'),('서문','서문'),('솔로문','솔로문'),('동문','동문'),('대학원동','대학원동'),
        ('화학관','화학관'),('향토/첨성','향토/첨성')
    )
    GENDER=(
        ('암컷','암컷'),('수컷','수컷')
    )
    TNR=(
        ('중성화YES','중성화YES'),('중성화NO','중성화NO')
    )
    COLOR=(
        ('치즈','치즈'),('고등어','고등어'),('삼색','삼색'),('검정','검정'),('카오스','카오스')
    )
    INTIMACY=(
        ('상','상'),('중','중'),('하','하')
       )
    subcategory=models.ManyToManyField(Subcategory,blank=True,related_name='cat')
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True,allow_unicode=True)
    image=models.ImageField(upload_to='cat/%Y/%m/%d',blank=True)
   
    gender=models.CharField(max_length=200,db_index=True,choices=GENDER)
    tnr=models.CharField(max_length=200,db_index=True,choices=TNR)
    domain=models.CharField(max_length=200,choices=DOMAIN)
    color=models.CharField(max_length=200,db_index=True,choices=COLOR)
    intimacy=models.CharField(max_length=200,db_index=True,choices=INTIMACY)
    
    description=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created']
        index_together=[['id','slug']]

    def __str__(self):
        return self.name
