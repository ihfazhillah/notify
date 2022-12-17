from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

class Tag(TimeStampedModel):
    title = models.CharField(max_length=255)

    # we use text field here, because the upwork text need more than 255 length
    url = models.TextField()


class Item(TimeStampedModel):
    tags = models.ManyToManyField(Tag, related_name="items")
    guid = models.TextField()
    content = models.TextField()
    title = models.CharField(max_length=255)
    published = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
