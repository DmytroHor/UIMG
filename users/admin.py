from django.contrib import admin

from . import models

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    pass


admin.site.register(models.User, UserAdmin)
