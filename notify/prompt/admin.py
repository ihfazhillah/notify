from django.contrib import admin

from notify.prompt.models import ProposalPrompt, GeneralPrompt

admin.site.register(ProposalPrompt, admin.ModelAdmin)
admin.site.register(GeneralPrompt, admin.ModelAdmin)
