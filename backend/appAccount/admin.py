from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", 'is_superuser', "is_active", 'created_date')
    list_filter = ("email", "is_staff", "is_active", 'is_superuser')
    fieldsets = (
        ("Basic Information", {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", 'is_superuser', "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("created_date", "updated_date", "last_login")}),
    )
    readonly_fields = (
        "created_date", "updated_date", "last_login"
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)