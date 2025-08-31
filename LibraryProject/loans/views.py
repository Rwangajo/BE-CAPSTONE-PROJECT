from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from .models import Loan
from .serializers import LoanSerializer, ReturnBookSerializer
from books.models import Book

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # List only loans for the logged-in user
        return Loan.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'], url_path='checkout')
    def checkout(self, request):
        """
        Borrow a book
        Expected JSON: { "book": <book_id> }
        """
        serializer = LoanSerializer(data={
            'user': request.user.id,
            'book': request.data.get('book')
        })
        serializer.is_valid(raise_exception=True)
        loan = serializer.save()
        return Response(LoanSerializer(loan).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='return')
    def return_book(self, request):
        """
        Return a borrowed book
        Expected JSON: { "book": <book_id> }
        """
        book_id = request.data.get('book')
        try:
            loan = Loan.objects.get(user=request.user, book_id=book_id, status='borrowed')
        except Loan.DoesNotExist:
            return Response({"error": "No active loan found for this book."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ReturnBookSerializer(loan, data={})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": f"Book '{loan.book.title}' returned successfully."}, status=status.HTTP_200_OK)


class CheckoutLoanAPIView(CreateAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReturnLoanAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        book_id = request.data.get('book')
        try:
            loan = Loan.objects.get(user=request.user, book_id=book_id, status='borrowed')
        except Loan.DoesNotExist:
            return Response({"error": "No active loan found for this book."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ReturnBookSerializer(loan, data={})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": f"Book '{loan.book.title}' returned successfully."}, status=status.HTTP_200_OK)


class UserLoansAPIView(ListAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Loan.objects.filter(user=self.request.user)
