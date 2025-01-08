# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields
    date_of_birth = models.DateField(null=True, blank=True)
    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.username

    
