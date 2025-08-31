from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'category', 'total_copies', 'copies_available')
    list_filter = ('category',)
    search_fields = ('title', 'author', 'isbn')

    # Dynamic field for available copies
    def copies_available(self, obj):
        # If you have a Loan model tracking loans, replace 0 with your calculation
        # Example: return obj.total_copies - obj.loan_set.count()
        return obj.total_copies  

    copies_available.short_description = "Copies Available"

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
