from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Q
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]  # 👈 only admin can modify
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "author", "isbn"]
    ordering_fields = ["title", "author", "published_date"]

    def get_queryset(self):
        qs = super().get_queryset()
        available = self.request.query_params.get("available")
        title = self.request.query_params.get("title")
        author = self.request.query_params.get("author")
        isbn = self.request.query_params.get("isbn")

        if available and available.lower() in ("true", "1", "yes"):
            qs = qs.filter(copies_available__gt=0)
        if title:
            qs = qs.filter(title__icontains=title)
        if author:
            qs = qs.filter(author__icontains=author)
        if isbn:
            qs = qs.filter(isbn__icontains=isbn)
        return qs
