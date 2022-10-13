from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from account.models import MyUser


class MyUserAdmin(UserAdmin):
    list_display = ("email", "username","picture")
    search_fields = ("email", "username",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets =()

admin.site.register(MyUser,MyUserAdmin)