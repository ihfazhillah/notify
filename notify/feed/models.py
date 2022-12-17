from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

class Tag(TimeStampedModel):
    title = models.CharField(max_length=255)
    url = models.URLField()


class Item(TimeStampedModel):
    tags = models.ManyToManyField(Tag, related_name="items")
    guid = models.TextField()
    content = models.TextField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
