from rest_framework import serializers

from notify.prompt.models import ProposalPrompt, GeneralPrompt, GeneralPromptRequest


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
            instance = ProposalPrompt.objects.create(**validated_data, user=request.user)

            if instance.selected:
                # make another not selected
                ProposalPrompt.objects.filter(
                    user=request.user
                ).exclude(pk=instance.id).update(selected=False)

            return instance


class RequestPromptBody(serializers.ModelSerializer):
    class Meta:
        model = GeneralPromptRequest
        fields = [
            "pk",
            "prompt",
            "additional_body",
            "duration",
            "error",
            "response"
        ]

    def create(self, validated_data):
        request = self.context.get("request")
        if request:
            instance = GeneralPromptRequest.objects.create(**validated_data, user=request.user)
            return instance
