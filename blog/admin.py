# Register your models here.
from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'post_id', 'author', 'creation_date']

class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'comment','published']
	list_editable = ['published']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_name', 'category_url']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(About)