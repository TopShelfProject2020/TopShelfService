from django.db import models
from authen.models import MyUser


class Review(models.Model):
    text = models.TextField(max_length=1500)
    written_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)