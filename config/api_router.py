from django.conf import settings
from django.urls import path
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

from notify.feed.api.views import ItemViewSet
from notify.prompt.api.views import ProposalPromptViewSet, request_prompt
from notify.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register('devices', FCMDeviceAuthorizedViewSet)
router.register("feed-items", ItemViewSet)
router.register("proposal-prompts", ProposalPromptViewSet)


app_name = "api"
urlpatterns = router.urls + [
    path("general-prompt-request/", request_prompt, name="request-general-prompt"),
]
