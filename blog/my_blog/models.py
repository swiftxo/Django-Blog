from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags
import html

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank = True, null = True)
    post_date = models.DateTimeField(auto_now_add = True)
    category = models.CharField(max_length = 255, default = 'unspecified')
    likes = models.ManyToManyField(User, related_name = 'blog_post')
    snippet  = models.CharField(max_length = 155, blank = True)
    header_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    
    def save(self, *args, **kwargs):
        if not self.snippet:
            clean_text = strip_tags(self.body)
            unescaped_text = html.unescape(clean_text)
            self.snippet = unescaped_text[:150] + '...' if self.body else 'No content'
        super().save(*args, **kwargs)


    def total_likes(self):
        return self.likes.count()


    def __str__ (self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("article-detail", args=[self.id])

class Profile(models.Model):
    user =  models.OneToOneField(User, null = True, on_delete= models.CASCADE)
    bio = models.TextField(max_length=3000,null=True,blank=True)
    profile_pic = models.ImageField(null = True, blank = True, upload_to = "images/profile/")
    instagram_link = models.CharField(max_length=255,null=True,blank=True)
    twitter_link = models.CharField(max_length=255,null=True,blank=True)
    website_link = models.CharField(max_length=255,null=True,blank=True)
    github_link = models.CharField(max_length=255,null=True,blank=True)
    discord_link = models.CharField(max_length=255,null=True,blank=True) 
    spotify_link = models.CharField(max_length=255,null=True,blank=True) 
    soundcloud_link = models.CharField(max_length=255,null=True,blank=True)
    youtube_link = models.CharField(max_length=255,null=True,blank=True) 





    def __str__ (self):
            return str(self.user)