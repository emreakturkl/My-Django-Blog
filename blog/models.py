#-*- coding: utf-8 -*-
# Create your models here.
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    nid = models.IntegerField(blank=True, null=True, verbose_name='Nid')
    author = models.ForeignKey('auth.User',blank=True, null=True, verbose_name="Yazar")
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name="Başlık")
    article = RichTextUploadingField(blank=True, null=True, verbose_name="Yazi")
    slug = models.SlugField(max_length=40, blank=True, null=True, verbose_name="Slug")
    creation_date = models.DateTimeField(default=timezone.now, verbose_name="Yaratılma Tarihi")
    keywords = models.TextField(blank=True, null=True, verbose_name="Keywords")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.ImageField(blank=True, null=True, verbose_name="Resim")

    def __unicode__(self):
        return '%s' %(self.title)

    def saves(self):
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class Comment(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True, verbose_name="İsim")
    email = models.EmailField(max_length=254, blank=False, null=True, verbose_name="E-posta")
    website = models.CharField(max_length=200, blank=False, null=True, verbose_name="İnternet Sitesi")
    comment = models.TextField(blank=False, null=True, verbose_name="Yorum")
    created_date = models.DateTimeField(default=timezone.now,verbose_name="Yaratılma Tarihi")
    slug  = models.CharField(max_length=200, blank=True, null=True, verbose_name="Slug")
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' %(self.name)

    def saves(self):
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']    

class Category(models.Model):
    category_name = models.CharField(max_length=200, blank=False, null=True, verbose_name="Kategori İsmi")
    category_url  = models.CharField(max_length=200, blank=False, null=True, verbose_name="Kategori Url")
    category_edit = RichTextUploadingField(blank=True, null=True, verbose_name="Düzenle") 
    category_keywords = models.TextField(blank=True, null=True, verbose_name="Kategori Keywords")
    category_description = models.TextField(blank=True, null=True, verbose_name="Kategori Description")

    def __unicode__(self):
        return '%s' %(self.category_name)

    def saves(self):
        self.save()

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ['id']

class About(models.Model):
    header_title   = models.CharField(max_length=200, blank=True, null=True, verbose_name="Header Title")
    header_contact = models.CharField(max_length=200, blank=True, null=True, verbose_name="Header Mail Url")
    header_twitter = models.CharField(max_length=200, blank=True, null=True, verbose_name="Header Twitter Url")
    header_linkedin = models.CharField(max_length=200, blank=True, null=True, verbose_name="Header Linkedin Url")
    header_github   = models.CharField(max_length=200, blank=True, null=True, verbose_name="Header Github Url")
    
    home_title   = models.CharField(max_length=200, blank=True, null=True, verbose_name="Anasayfa Başlık")
    home_image   = models.ImageField(blank=True, null=True, verbose_name="Anasayfa Resmi")
    home_text    = models.TextField(blank=True, null=True, verbose_name="Anasayfa Yazısı")
    home_twitter = models.TextField(blank=True, null=True, verbose_name="Twitter Url")
    
    about_image  = models.ImageField(blank=True, null=True, verbose_name="Hakkımda Resmi")
    about_text   = models.TextField(blank=True, null=True, verbose_name="Hakkımda Yazısı")
    about_social = models.TextField(blank=True, null=True, verbose_name="Hakkımda Linkleri")
    
    footer_text   = models.CharField(max_length=200, blank=True, null=True, verbose_name="Footer Yazisi")
    footer_text_url = models.CharField(max_length=200, blank=True, null=True, verbose_name="Footer Url")
    footer_image = models.ImageField(blank=True, null=True, verbose_name="Footer Resmi")
    favicon = models.ImageField(blank=True, null=True, verbose_name="Favicon Resmi")

    def __unicode__(self):
        return '%s' %("Website Settings")

    def saves(self):
        self.save()

    def __str__(self):
        return '%s'%("Website Settings")

    class Meta:
        ordering = ['id']
