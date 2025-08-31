from rest_framework import serializers
from django.utils import timezone
from .models import Loan
from books.models import Book
from users.models import User

class LoanSerializer(serializers.ModelSerializer):
    # Show book title for frontend convenience
    book_title = serializers.CharField(source='book.title', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Loan
        fields = ['id', 'book', 'book_title', 'user', 'username', 'borrow_date', 'return_date', 'status']
        read_only_fields = ['borrow_date', 'return_date', 'status']

    def create(self, validated_data):
        user = validated_data['user']
        book = validated_data['book']

        # Check if the user already has this book borrowed and not returned
        if Loan.objects.filter(user=user, book=book, status='borrowed').exists():
            raise serializers.ValidationError("You have already borrowed this book.")

        # Check if copies are available
        if book.copies_available <= 0:
            raise serializers.ValidationError("No copies available for this book.")

        # Reduce available copies
        book.copies_available -= 1
        book.save()

        # Create loan
        return super().create(validated_data)


class ReturnBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['status']
        read_only_fields = []

    def update(self, instance, validated_data):
        instance.status = 'returned'
        instance.return_date = timezone.now()
        instance.save()
        # Increase available copies
        instance.book.copies_available += 1
        instance.book.save()
        return instance
