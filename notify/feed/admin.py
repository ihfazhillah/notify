from django.contrib import admin
from notify.feed.models import Tag, Item

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ["title", "url"]


admin.site.register(Tag, TagAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ["tags", "guid", "title", "description"]


admin.site.register(Item, ItemAdmin)
