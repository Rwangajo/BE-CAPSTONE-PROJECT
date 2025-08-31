# loans/admin.py
from django.contrib import admin
from .models import Loan

class LoanAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'status')
    list_filter = ('status', 'borrow_date')  # These must match model fields
    search_fields = ('user__username', 'book__title')  # Optional but helpful

admin.site.register(Loan, LoanAdmin)
