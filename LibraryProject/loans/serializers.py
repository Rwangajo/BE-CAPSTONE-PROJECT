from rest_framework import serializers
from .models import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ["id", "user", "book", "borrow_date", "return_date", "status"]
        read_only_fields = ["borrow_date", "return_date", "status"]
