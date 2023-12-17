from django.contrib import admin
from appTodo.models import Job


@admin.register(Job)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name", "status"]
    list_filter = ["user", "status"]
    list_display_links = ["id"]
