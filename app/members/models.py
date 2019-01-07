from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    img_profile = models.ImageField(
        '프로필 이미지',
        upload_to='user',
        blank=True,
        null=True,
    )
