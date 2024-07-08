from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_entry.api.views import JournalEntryViewSet,CategoryViewSet

router = DefaultRouter()
router.register("journal entry", JournalEntryViewSet, basename="journal entry")
router.register("category", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls) ),
]