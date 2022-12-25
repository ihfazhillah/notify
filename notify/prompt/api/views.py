from django.db.models import QuerySet
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from notify.prompt.api.serializers import ProposalPromptSerializer
from notify.prompt.models import ProposalPrompt


class ProposalPromptViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = ProposalPrompt.objects.all()
    serializer_class = ProposalPromptSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(
            user=self.request.user
        )

    @action(methods=["POST"], detail=True, url_name="activate")
    def activate(self, request, pk=None):
        instance = self.get_object()

        self.get_queryset().exclude(
            id=instance.id
        ).update(selected=False)

        instance.selected = True
        instance.save()

        instance.refresh_from_db()

        serializer = self.get_serializer_class()(instance=instance)

        return Response(serializer.data)
