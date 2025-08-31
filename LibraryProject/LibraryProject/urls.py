from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API Endpoints
    path('api/', include('books.urls')),   # /api/books/
    path('api/', include('users.urls')),   # /api/users/, /api/token/
    path('api/', include('loans.urls')),   # /api/loans/
]
