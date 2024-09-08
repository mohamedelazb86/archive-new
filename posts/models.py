from django.db import models
from taggit.managers import TaggableManager

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
    user=models.ForeignKey(User,related_name='post_user',on_delete=models.CASCADE)
    title=models.CharField(max_length=120,verbose_name=_('name'))
    image=models.ImageField(upload_to='photo_post')
    content=models.TextField(max_length=1500)
    publish_date=models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
    slug=models.SlugField(null=True,blank=True)
    category=models.ForeignKey('Category',related_name='post_category',on_delete=models.SET_NULL,null=True,blank=True)
    draft=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)


class Category(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Review(models.Model):
    user=models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True,blank=True)
    post=models.ForeignKey(Post,related_name='review_post',on_delete=models.CASCADE)
    rate=models.IntegerField(choices=[(i,i) for i in range(1,6)])
    publish_date=models.DateTimeField(default=timezone.now)
    content=models.TextField(max_length=750)

    def __str__(self):
        return f'{self.user}  &&& {self.post}'
