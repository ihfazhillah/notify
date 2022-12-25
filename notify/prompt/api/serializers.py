from rest_framework import serializers

from notify.prompt.models import ProposalPrompt


class ProposalPromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalPrompt
        fields = (
            "id",
            "label",
            "text",
            "selected",
        )
