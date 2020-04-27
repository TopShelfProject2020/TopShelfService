from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
logger = logging.getLogger('api')
from main.models import Book,Publisher


@receiver(post_save, sender=Publisher)
def publisher_created(sender, instance, created, **kwargs):
    if created:
        Book.objects.create(publisher=instance, title="title",num_pages = 123,)
        logger.info(f'Book signal works')

