from django.contrib import admin

from .models import MenuPoint


admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Древовидное меню'


@admin.register(MenuPoint)
class MenuPointAdmin(admin.ModelAdmin):
    list_display = ['title', 'menu_name', 'parent', 'url', 'named_url']
    list_display_links = ['title']
    ordering = ['menu_name', 'title']
    list_filter = ['menu_name']
    search_fields = ['title', 'url', 'named_url']