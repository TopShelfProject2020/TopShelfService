from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from authen.models import MyUser


class Profile(models.Model):
    MODERATOR = 1
    READER = 2
    WRITER = 3
    ROLE_CHOICES = (
        (MODERATOR, 'moderator'),
        (READER, 'reader'),
        (WRITER, 'writer'),
    )
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    objects = models.Manager()

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username
