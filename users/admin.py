from django.contrib import admin

from .forms import UserForm


class UserAdmin(admin.ModelAdmin):
    form = UserForm
    # view_on_site = False

    search_fields = ('user_name', 'email')

    list_display = (
        'pk',
        'user_name',
        'email',
        'time_created',
        'last_login',
        'is_admin',
    )

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'gender', 'date_of_birth', 'address')
        }),
        ('Auth Info', {
            'fields': ('user_name', 'mobile', 'email', 'password')
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


admin.site.register(UserAdmin)
