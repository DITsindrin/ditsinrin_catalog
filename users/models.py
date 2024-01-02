from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name='телефон')
    avatar = models.ImageField(upload_to='users/', default='default.png', verbose_name='аватар')
    country = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name='страна')
    is_active = models.BooleanField(default=False, verbose_name='признак верификации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
