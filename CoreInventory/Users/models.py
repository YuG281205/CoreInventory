from django.db import models
from django.contrib.auth.hashers import make_password
import random
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password


class User(models.Model):

    ROLE_CHOICES = (
        ('manager', 'Inventory Manager'),
        ('staff', 'Warehouse Staff'),
    )

    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # Email verification fields
    otp = models.IntegerField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        """Generate 6 digit OTP"""
        self.otp = random.randint(100000, 999999)

    def save(self, *args, **kwargs):

        # hash password before saving
        if not self.password.startswith('pbkdf2'):
            self.password = make_password(self.password)

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
    
