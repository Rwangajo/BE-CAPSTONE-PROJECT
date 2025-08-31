from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # API Endpoints
    path('api/', include('books.urls')),   # /api/books/
    path('api/', include('users.urls')),   # /api/users/, /api/token/
    path('api/', include('loans.urls')),   # /api/loans/
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('borrow/', views.borrow_page, name='borrow_page'),
    path('logout/', views.logout_user, name='logout'),
]
