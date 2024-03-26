from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from PIL import Image


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile(user = instance)

@receiver(post_save, sender=Profile)
def compress_image_quality(sender, instance, **kwargs):
    img = Image.open(instance.image.path)

    # Adjust the quality parameter based on your preferences (0 to 100)
    img.save(instance.image.path, quality=20)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()

