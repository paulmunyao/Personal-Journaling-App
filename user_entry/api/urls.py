from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_entry.api.views import JournalEntryViewSet,CategoryViewSet

router = DefaultRouter()
router.register("journal-entry", JournalEntryViewSet, basename="journal-entry")
router.register("journal-entry/<int:item-id>", JournalEntryViewSet, basename="journal-entry-item")
router.register("category", CategoryViewSet, basename="category")
router.register("category/<int:item-id>", CategoryViewSet, basename="category-item")
router.register("summary",JournalEntryViewSet, basename="summary")

urlpatterns = [
    path("", include(router.urls) ),
]