from django.conf import settings
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

from notify.feed.api.views import ItemViewSet
from notify.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register('devices', FCMDeviceAuthorizedViewSet)
router.register("feed-items", ItemViewSet)


app_name = "api"
urlpatterns = router.urls
