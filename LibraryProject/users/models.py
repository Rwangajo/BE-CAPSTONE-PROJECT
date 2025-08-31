from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (("admin", "Admin"), ("user", "User"))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")
    date_of_membership = models.DateField(auto_now_add=True)  # required in spec
    # Active status is built-in as `is_active`

    def __str__(self):
        return self.username
