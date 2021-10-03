from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ImportExportActionModelAdmin

from .models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin, ImportExportActionModelAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "last_login",
        "date_joined",
        "is_staff",
        "is_active",
    )

    ordering = ("-date_joined",)
    list_display_links = ("email",)
    list_per_page = 25
    readonly_fields = ("date_joined", "last_login")

    fieldsets = (
        (_("Credential"), {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "username", "phone_number")},
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (
            _("Permissions"),
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_admin",
                    "is_superuser",
                ),
            },
        ),
    )
    add_fieldsets = (
        (_("Credentials"), {"fields": ("email", "password1", "password2")}),
        (
            _("Personal data"),
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "username", "phone_number"),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
        (
            _("Permissions"),
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_admin",
                    "is_superuser",
                ),
            },
        ),
    )


