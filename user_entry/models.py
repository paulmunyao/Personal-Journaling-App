from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    def _str_(self):
        return self.name
class JournalEntry(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.title

class Summary(models.Model):
    entry_count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return f"Summary for {self.category.name} - {self.entry_count} entries"