from django.contrib import admin

from notify.prompt.models import ProposalPrompt

admin.site.register(ProposalPrompt, admin.ModelAdmin)
