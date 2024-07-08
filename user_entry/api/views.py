from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from user_entry.models import JournalEntry
from user_entry.api.serializers import JournalEntrySerializer,CategorySerializer

class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]