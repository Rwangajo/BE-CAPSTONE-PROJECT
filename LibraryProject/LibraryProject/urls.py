from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.views import BookViewSet
from users.views import UserViewSet
from loans.views import LoanViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import TemplateView  # optional for simple templates

# Router for DRF ViewSets
router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'users', UserViewSet, basename='users')
router.register(r'loans', LoanViewSet, basename='loans')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', include('users.urls')),
    path('api/books/', include('books.urls')),
    path('api/loans/', include('loans.urls')),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('login/', TemplateView.as_view(template_name="login.html"), name='login'),
    path('register/', TemplateView.as_view(template_name="register.html"), name='register'),
    path('borrow/', TemplateView.as_view(template_name="borrow.html"), name='borrow'),

    
]
