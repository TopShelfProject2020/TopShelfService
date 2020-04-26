from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

from main.models import Card, Order


class MyUserManager(UserManager):
    pass


class MyUserBase(AbstractUser):
    pass

    # class Meta:
    #     abstract = True


class MyUser(MyUserBase):
    address = models.CharField(max_length=255)
    card_info = models.ForeignKey(Card, on_delete=models.CASCADE)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)


class Moderator(MyUserBase):
    pass