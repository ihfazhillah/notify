import datetime
import traceback

from django.db import models
from django.db.models import JSONField
from model_utils.models import TimeStampedModel

from notify.users.models import User


class ProposalPrompt(TimeStampedModel):
    text = models.TextField()
    label = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Per user only one that active
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.label


class GeneralPrompt(TimeStampedModel):
    """
    Used for general prompt. the type should unique.
    """
    prompt_type = models.CharField(max_length=255, unique=True)
    text = models.TextField()

    def __str__(self):
        return self.prompt_type


class GeneralPromptRequest(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prompt_requests")
    prompt = models.ForeignKey(
        GeneralPrompt,
        on_delete=models.CASCADE,
        related_name="requests"
    )
    additional_body = models.TextField()

    duration = models.DurationField(null=True, blank=True)
    error = models.TextField(null=True, blank=True)
    response = JSONField(null=True, blank=True)

    def process(self):
        from notify.utils.proposal import gpt3_openai
        start = datetime.datetime.now()
        prompt = f"{self.prompt.text}\n{self.additional_body}\n\n"
        try:
            response = gpt3_openai(prompt)
            self.response = response
        except Exception as e:
            # for now just record the error
            self.error = traceback.format_exc()

        end = datetime.datetime.now()
        self.duration = end - start
        self.save()
