from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class BookshelfManager(BaseUserManager):
    """
    Modified Manager with autofilling register date.
    """
    def _create_user(self, username, email, password, **kwargs):
        if not username:
            raise ValueError('username required')
        if not email:
            raise ValueError('email required')
        user = self.model(
            username=username,
            email=email,
            register_date=datetime.now(),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **kwargs)

    def create_superuser(self, username, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **kwargs)


class BookshelfUser(AbstractBaseUser):
    """
    Modified AbstractBaseUser model required username and email fields.
    Register date fills automatically.
    """
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    register_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email'
    ]

    objects = BookshelfManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
