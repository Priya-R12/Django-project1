from django.contrib import admin
from . models import Post

# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ["post_title", "post_image", "post_id" , "post_at" , "user"]
