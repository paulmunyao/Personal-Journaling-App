from django.db import models
from django.contrib.auth.models import User

class JournalEntry(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=1000)
    category = models.CharField(max_length=20)
    date = models.DateTimeField

    def __str__(self):
        return self.title
