from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    available_copies = models.IntegerField(default=1)
    total_copies = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"
