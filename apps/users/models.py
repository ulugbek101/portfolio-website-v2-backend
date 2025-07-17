from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(
        verbose_name=_('E-mail address'),
        unique=True,
        max_length=255,
    )
    first_name = models.CharField(
        verbose_name=_('First name'),
        max_length=255,
    )
    last_name = models.CharField(
        verbose_name=_('Last name'),
        max_length=255,
    )
    profile_image = models.ImageField(
        verbose_name=_('Profile image'),
        upload_to='users/',
        default='users/user-default.png',
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='unique_first_name_and_last_name',
                fields=['first_name', 'last_name']
            )
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
