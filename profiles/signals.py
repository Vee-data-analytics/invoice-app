from django.db.models.signals import post_save
from django.dispatch import receiver
from.models import Profiles
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print(sender)
    print(instance)
    print(created)

    if created:
        Profiles.objects.create(user=instance)