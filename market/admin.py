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

    readonly_fields = ('time_created', 'time_modified', 'time_deleted', 'deleted')

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


admin.site.register(Stock, StockAdmin)
