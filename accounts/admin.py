from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm, User


User = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = User
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['username', 'email', 'user_type']

    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('user_type',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + \
        ((None, {'fields': ('user_type',)}),)


admin.site.register(User, CustomUserAdmin)
