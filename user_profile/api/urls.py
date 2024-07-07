from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_profile.api.views import ProfileViewSet

router = DefaultRouter()
router.register("profile", ProfileViewSet, basename="profile")

urlpatterns = [
    path("", include(router.urls) ),
]