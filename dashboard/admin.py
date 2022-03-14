from django.contrib import admin

from dashboard.models import Pages, SelectTemplate, FavIcon, MainIcon, PageTitle

class DashboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'is_active')

class MainIconAdmin(admin.ModelAdmin):
    list_display = ('id', 'active_template', 'image')

class FaviconAdmin(admin.ModelAdmin):
    list_display = ('id', 'active_template', 'image')

class PageTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'active_template', 'title')

admin.site.register(Pages)
admin.site.register(PageTitle, PageTitleAdmin)
admin.site.register(SelectTemplate, DashboardAdmin)
admin.site.register(FavIcon, FaviconAdmin)
admin.site.register(MainIcon, MainIconAdmin)

