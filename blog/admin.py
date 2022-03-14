from django.contrib import admin

from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)

admin.site.register(Blog, BlogAdmin)