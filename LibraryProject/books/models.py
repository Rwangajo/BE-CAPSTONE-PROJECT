from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, blank=True, null=True)  # Optional
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    total_copies = models.PositiveIntegerField(default=1)  # Total copies of the book

    def __str__(self):
        return self.title
