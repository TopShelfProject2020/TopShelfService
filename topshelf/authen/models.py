from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser


class MyUserManager(UserManager):
    pass


class MyUser(AbstractUser):
    ROLE_MODERATOR = 0
    ROLE_WRITER = 1
    ROLE_READER = 2

    ROLE_CHOICES = (
        (ROLE_MODERATOR, 'moderator'),
        (ROLE_WRITER, 'writer'),
        (ROLE_READER, 'reader'),
    )


