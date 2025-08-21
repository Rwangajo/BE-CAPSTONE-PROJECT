from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('user', 'User')], default='user')

    def __str__(self):
        return self.username

AUTH_USER_MODEL = 'users.User'
