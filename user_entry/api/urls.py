from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_entry.api.views import JournalEntryViewSet

router = DefaultRouter()
router.register("journal entry", JournalEntryViewSet, basename="journal entry")

urlpatterns = [
    path("", include(router.urls) ),
]