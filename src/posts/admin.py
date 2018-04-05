from django.contrib import admin
from .models import Post
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title','updated','timestamp']
	list_display_links = ['updated']
	search_fields = ['title','content']
	list_editable = ['title']
	list_filter = ['title','timestamp']
	class meta:
			model = Post
			

admin.site.register(Post, PostModelAdmin)
