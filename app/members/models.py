from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    visited = models.DateTimeField(auto_now=True)