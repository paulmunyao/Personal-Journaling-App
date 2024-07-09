from rest_framework import serializers
from user_entry.models import JournalEntry, Category, Summary


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class JournalEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = JournalEntry
        fields = "__all__"

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = "_all_"