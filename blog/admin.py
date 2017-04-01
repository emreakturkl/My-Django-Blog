# Register your models here.
from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'nid', 'author', 'slug', 'creation_date')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'website')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_name', 'category_url')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(About)