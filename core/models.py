from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True , blank = False)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active =  models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=300, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=50, null=True)
