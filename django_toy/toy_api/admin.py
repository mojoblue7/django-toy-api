from django.contrib import admin

# Register your models here.
from .models import UserInfo


@admin.register(UserInfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'gender', 'reg_date', 'mod_date']
    list_display_links = ['id', 'email', 'username', 'gender', 'reg_date', 'mod_date']
