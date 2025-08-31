from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Loan
from .serializers import LoanSerializer
from books.models import Book


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Handle borrowing a book."""
        book = serializer.validated_data['book']

        # check availability
        if book.copies_available <= 0:
            raise ValueError("This book is not available for borrowing.")

        # decrease copies
        book.copies_available -= 1
        book.save()

        # save loan record with user + borrowed_date
        serializer.save(user=self.request.user, borrowed_date=timezone.now())

    def update(self, request, *args, **kwargs):
        """Handle returning a book."""
        instance = self.get_object()

        if 'returned_date' in request.data and not instance.returned_date:
            # returning a book
            instance.returned_date = timezone.now()
            instance.book.copies_available += 1
            instance.book.save()
            instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
