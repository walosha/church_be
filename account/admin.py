from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ChurchGroup


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("password",)}),
        ("Personal info", {
         "fields": ("firstname", "lastname", "email", "category")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    add_form = CustomUserCreationForm  # Here
    form = CustomUserChangeForm  # Here
    change_password_form = AdminPasswordChangeForm  # Here
    list_display = ("email", "firstname", "lastname", "is_staff", "category")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("firstname", "lastname", "email")
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(CustomUser, CustomUserAdmin)  # Here

admin.site.register(ChurchGroup)  # Here
