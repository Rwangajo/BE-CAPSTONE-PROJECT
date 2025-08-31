from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)  # unique ISBN
    published_date = models.DateField(default="2000-01-01")
    copies_available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.author}"
