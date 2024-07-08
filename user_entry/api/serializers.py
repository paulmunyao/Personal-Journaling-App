from rest_framework import serializers
from user_entry.models import JournalEntry,Category

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Category
        fields = "__all__"