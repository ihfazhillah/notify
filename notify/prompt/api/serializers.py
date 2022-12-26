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

    def create(self, validated_data):
        request = self.context.get('request')
        if request:
            instance = ProposalPrompt.objects.ceate(**validated_data, user=request.user)
            return instance


