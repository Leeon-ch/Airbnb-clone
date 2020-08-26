from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Model Admin is for the Model we import
# @admin.register(models.User)
# class CustomUserAdmin(admin.ModelAdmin):

#     """ Custom User Admin """

#     list_display = ("username", "email", "gender",
#                     "language", "currency", "superhost")
#     list_filter = ("language", "currency", "superhost")

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    # UserAdmin has filedsets which show things on the admin panel
    """ Custom User Admin """

    list_display = ("username", "email", "gender",
                    "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
