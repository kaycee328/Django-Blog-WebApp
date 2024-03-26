from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib import messages
from .models import Post


@receiver(post_delete, sender=Post)
def message(sender, instance, **kwargs):
    print(f"'{instance.title}' has been removed!")
    

# @receiver(post_save, sender=Profile)
# def compress_image_quality(sender, instance, **kwargs):
#     img = Image.open(instance.image.path)

#     # Adjust the quality parameter based on your preferences (0 to 100)
#     img.save(instance.image.path, quality=20)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, created, **kwargs):
#     instance.profile.save()