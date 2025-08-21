from django.db import models
from books.models import Book
from users.models import User

class Loan(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrowed')

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.status})"
