from django.contrib import admin
from notify.feed.models import Tag, Item, ItemAccess, UpworkSkill, UpworkItemCategory, UpworkItem, ProposalExample


# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ["title", "url"]


admin.site.register(Tag, TagAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ["guid", "title", "content"]


admin.site.register(Item, ItemAdmin)


class ItemAccessAdmin(admin.ModelAdmin):
    list_display = ["user", "created"]


admin.site.register(ItemAccess, ItemAccessAdmin)


class UpworkSkillAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(UpworkSkill, UpworkSkillAdmin)


class UpworkCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(UpworkItemCategory, UpworkSkillAdmin)


class UpworkFeedItem(admin.ModelAdmin):
    list_display = ["description", "budget", "hourly_range"]

admin.site.register(UpworkItem, UpworkFeedItem)


class UpworkProposalAdmin(admin.ModelAdmin):
    list_display = ["item", "text"]




admin.site.register(ProposalExample, UpworkProposalAdmin)
