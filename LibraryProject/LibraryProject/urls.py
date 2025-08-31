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

# Router for DRF ViewSets
router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'users', UserViewSet, basename='users')
router.register(r'loans', LoanViewSet, basename='loans')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
