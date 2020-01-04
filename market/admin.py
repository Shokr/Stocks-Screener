from django.contrib import admin

from .forms import *


class StockAdmin(admin.ModelAdmin):
    form = StockForm

    search_fields = ('symbol', 'name')

    list_display = (
        'pk',
        'symbol',
        'name',
        'sector',
    )

    readonly_fields = ('time_created', 'time_modified', 'time_deleted', 'deleted', 'creator')

    fieldsets = (
        ('Stock Data', {
            'fields': ('symbol', 'name', 'sector')
        }),
        ('Info', {
            'fields': ('info', 'creator', 'deleted')
        }),
        ('Timeline', {
            'fields': ('time_created', 'time_modified', 'time_deleted')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.creator = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Stock, StockAdmin)
