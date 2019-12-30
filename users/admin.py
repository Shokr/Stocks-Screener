from django.contrib import admin

from .forms import *


class UserAdmin(admin.ModelAdmin):
    form = UserForm
    # view_on_site = False

    search_fields = ('username', 'email')

    list_display = (
        'pk',
        'username',
        'email',
        'time_created',
        'last_login',
        'is_admin',
    )

    readonly_fields = ('time_created', 'time_modified', 'last_login')

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'gender', 'date_of_birth', 'address')
        }),
        ('Auth Info', {
            'fields': ('username', 'mobile', 'email', 'password')
        }),
        ('Timeline', {
            'fields': ('time_created', 'time_modified', 'last_login')
        }),
        ('State', {
            'fields': ('is_active', 'is_admin')
        }),
    )

    # def has_delete_permission(self, request, obj=None):
    #     return False


admin.site.register(User, UserAdmin)
