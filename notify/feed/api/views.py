# list feed paginated
# log access
from django.contrib.postgres.aggregates import ArrayAgg
from django.db import models
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from notify.feed.api.serializers import ItemSerializer, SimpleItemSerializer, MyProposalSerializer, \
    MyProposalBodySerializer
from notify.feed.models import Item, ItemAccess, ProposalExample, MyProposal
from notify.utils.proposal import generate_proposal


class ItemViewSet(ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return SimpleItemSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        qs = super().get_queryset().order_by("-created")
        qs = qs.annotate(
            access_count=models.Count("itemaccess", filter=models.Q(itemaccess__user=self.request.user)),
            accessed=models.Case(
                models.When(access_count__gt=0, then=models.Value(True)),
                default=models.Value(False),
                output_field=models.BooleanField()
            ),
            proposal_example_text=models.F("proposal_example__text"),
            description=models.F("upwork__description"),
            budget=models.F("upwork__budget"),
            hourly_range=models.F("upwork__hourly_range"),
            category=models.F("upwork__category__name"),
            posted_on=models.F("upwork__posted_on"),
            country=models.F("upwork__country"),
            skills=ArrayAgg(models.F("upwork__skills__name"))
        )
        return qs

    @action(detail=True)
    def log_access(self, request, pk=None):
        instance = self.get_object()
        ItemAccess.objects.get_or_create(item=instance, user=self.request.user)
        return Response({"ok": True})

    @action(detail=True, methods=["POST"])
    def generate_proposal(self, request, pk):
        instance = self.get_object()
        proposal = generate_proposal(pk, self.request.user.id)
        ProposalExample.objects.update_or_create(
            item=instance, defaults={"text": proposal}
        )
        return Response({"proposal": proposal})

    @action(detail=True, methods=["GET"])
    def my_proposal(self, request, pk):
        instance = self.get_object()
        proposal, _ = MyProposal.objects.get_or_create(
            user=self.request.user,
            item=instance
        )
        return Response(
            MyProposalSerializer(instance=proposal).data
        )

    @action(detail=True, methods=["POST"])
    def update_my_proposal(self, request, pk):
        instance = self.get_object()
        proposal, _ = MyProposal.objects.get_or_create(
            user=self.request.user,
            item=instance
        )
        serializer = MyProposalBodySerializer(instance=proposal, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        proposal.refresh_from_db()

        return Response(
            MyProposalSerializer(instance=proposal).data
        )



