from django.db import models
from django.contrib.auth.models import User

class JournalEntry(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=1000)
    category = models.CharField(max_length=20)
    date = models.DateTimeField

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name

class Summary(models.Model):
    entry_count = models.IntegerField
    category_count = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField

    def __str__(self):
        return self.entry_count
