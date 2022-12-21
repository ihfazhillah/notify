# list feed paginated
# log access
from django.contrib.postgres.aggregates import ArrayAgg
from django.db import models
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from notify.feed.api.serializers import ItemSerializer, SimpleItemSerializer
from notify.feed.models import Item, ItemAccess


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
