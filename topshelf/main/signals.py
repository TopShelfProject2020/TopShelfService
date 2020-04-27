from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Book,Publisher


@receiver(post_save, sender=Publisher)
def publisher_created(sender, instance, created, **kwargs):
    if created:
        Book.objects.create(publisher=instance, title="asd")

