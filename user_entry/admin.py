from django.contrib import admin
from user_entry.models import JournalEntry, Category, Summary

admin.site.register(JournalEntry)
admin.site.register(Category)
admin.site.register(Summary)
