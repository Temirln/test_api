from django.contrib import admin

from .models import CustomUser, Order, Product
from django.contrib.auth.admin import UserAdmin 
from django.utils.translation import gettext_lazy as _

# Register your models here.

class UserAdminConfig(UserAdmin):
    ordering = ('email',)
    search_fields = ("email","username")
    list_display = ("email","username","last_login","date_joined","is_active","is_staff","is_admin","is_superuser")

    fieldsets = (
        (None, {"fields": ('email',"username", "password")}),
        # (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
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
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('email',"username", "password1", "password2"),
            },
        ),
    )


    readonly_fields=['date_joined','last_login']


admin.site.register(CustomUser,UserAdminConfig)
admin.site.register(Product)
admin.site.register(Order)
