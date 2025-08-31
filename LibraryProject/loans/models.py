from django.db import models
from django.utils import timezone
from django.conf import settings
from books.models import Book

class Loan(models.Model):
    STATUS_CHOICES = (("borrowed", "Borrowed"), ("returned", "Returned"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="loans")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="borrowed")

    class Meta:
        # Prevent duplicate active (unreturned) loans for same user-book
        constraints = [
            models.UniqueConstraint(
                fields=["user", "book", "status"],
                condition=models.Q(status="borrowed"),
                name="unique_active_loan_per_user_book",
            ),
        ]

    def mark_returned(self):
        self.status = "returned"
        self.return_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.user} -> {self.book} ({self.status})"
