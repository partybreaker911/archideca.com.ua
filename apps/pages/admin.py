from django.contrib import admin

from apps.pages.models import Page, Tags


class PageAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "timestamp",
    ]
    search_fields = [
        "title",
    ]
    list_filter = [
        "tag__tag_name",
    ]


admin.site.register(Page, PageAdmin)
admin.site.register(Tags)
