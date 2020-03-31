from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=255)