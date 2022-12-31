from django.contrib import admin

from notify.prompt.models import ProposalPrompt, GeneralPrompt, GeneralPromptRequest

admin.site.register(ProposalPrompt, admin.ModelAdmin)
admin.site.register(GeneralPrompt, admin.ModelAdmin)


class PromptRequestAdmin(admin.ModelAdmin):
    list_filter = ["user", "prompt"]
    list_display = ["user", "prompt", "additional_body", "duration", "error", "response"]


admin.site.register(GeneralPromptRequest, PromptRequestAdmin)
