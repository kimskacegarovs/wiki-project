from django.contrib import admin
from wiki_app.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']


admin.site.register(Page, PageAdmin)
