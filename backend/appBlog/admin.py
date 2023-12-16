from django.contrib import admin
from appBlog.models import Post, Category, Contact, Comment
from django_summernote.admin import SummernoteModelAdmin


class SummernoteAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "published_date", "status"]
    list_filter = ["author", "status"]
    list_display_links = ["id", "title"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "subject", "created_date"]
    date_hierarchy = "created_date"
    list_filter = ["email"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "post",
        "email",
        "subject",
        "created_date",
        "updated_date",
        "allowed",
    ]
    list_filter = ["post", "allowed"]
    list_display_links = ["id", "name"]
