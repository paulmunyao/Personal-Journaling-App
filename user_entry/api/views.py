from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets,filters
from user_entry.models import JournalEntry
from user_entry.api.serializers import JournalEntrySerializer,CategorySerializer

class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['categories']
    search_fields = ['title', 'category', 'date']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]