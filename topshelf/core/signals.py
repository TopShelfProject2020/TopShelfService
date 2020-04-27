from authen.models import MyUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Profile


@receiver(post_save, sender=MyUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=MyUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()