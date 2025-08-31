from django.urls import path
from .views import CheckoutLoanAPIView, ReturnLoanAPIView, UserLoansAPIView

urlpatterns = [
    path('checkout/', CheckoutLoanAPIView.as_view(), name='checkout'),
    path('return/', ReturnLoanAPIView.as_view(), name='return'),
    path('user/', UserLoansAPIView.as_view(), name='user-loans'),
]
