import uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core_apps.users.managers import CustomUserManager


class User(AbstractUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("username"), max_length=255, db_index=True, unique=True)
    first_name = models.CharField(verbose_name=_("first name"), max_length=100)
    last_name = models.CharField(verbose_name=_("last name"), max_length=100)
    email = models.EmailField(
        verbose_name=_("Email address"), db_index=True, unique=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    data_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "last_name", "first_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("user")

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def get_short_name(self):
        return self.first_name
