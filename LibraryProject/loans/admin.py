from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrow_date', 'return_date', 'status')
    list_filter = ('status', 'borrow_date', 'return_date')
    search_fields = ('book__title', 'user__username')
    ordering = ('-borrow_date',)
