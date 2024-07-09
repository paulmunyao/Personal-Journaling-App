from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_profile.api.views import ProfileViewSet

router = DefaultRouter()
router.register("profile", ProfileViewSet, basename="profile")
router.register("profile/<int:item-id>", ProfileViewSet, basename="profile-item")

urlpatterns = [
    path("", include(router.urls) ),
]