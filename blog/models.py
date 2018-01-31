from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User',blank=True, null=True, verbose_name="Yazar")
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name="Başlık")
    article = RichTextUploadingField(blank=True, null=True, verbose_name="Yazi")
    slug = models.SlugField(unique=True, editable=False, null=True, max_length=130, verbose_name="Slug")
    keywords = models.TextField(blank=True, null=True, verbose_name="Keywords")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.ImageField(blank=True, null=True, verbose_name="Resim")
    creation_date = models.DateTimeField(auto_now_add=False, verbose_name="Yaratılma Tarihi")

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug = slug
        counter = 1
        while (Post.objects.filter(slug=unique_slug).exists()):
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE, related_name="comments", null=True, verbose_name=None)
    name = models.CharField(max_length=200, blank=False, null=True, verbose_name="İsim")
    email = models.EmailField(max_length=254, blank=False, null=True, verbose_name="E-posta")
    comment = models.TextField(blank=False, null=True, verbose_name="Yorum")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Yaratılma Tarihi")
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']  

    def __str__(self):
        return self.name
      

class Category(models.Model):
    category_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Kategori İsmi")
    category_url  = models.CharField(max_length=200, blank=True, null=True, verbose_name="Kategori Url")
    category_edit = RichTextUploadingField(blank=True, null=True, verbose_name="Düzenle") 
    category_keywords = models.TextField(blank=True, null=True, verbose_name="Kategori Keywords")
    category_description = models.TextField(blank=True, null=True, verbose_name="Kategori Description")
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

    def __str__(self):
        return '%s'%("Website Settings")

    class Meta:
        ordering = ['id']
