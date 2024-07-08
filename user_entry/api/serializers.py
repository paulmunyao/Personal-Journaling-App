from rest_framework import serializers
from user_entry.models import JournalEntry

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = "__all__"