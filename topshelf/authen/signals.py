# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from authen.models import MyUser
# from main.models import AudioBook
#
#
# @receiver(post_save, sender=MyUser)
# def audio_created(sender, instance, created, **kwargs):
#     if created:
#         AudioBook.objects.create(user=instance)
