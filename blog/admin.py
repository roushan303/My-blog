from django.contrib import admin

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "content", "updated", "timestamp"]
	list_editable = ["title"]

	list_display_links = ["content"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post
admin.site.register(Post, PostModelAdmin)

