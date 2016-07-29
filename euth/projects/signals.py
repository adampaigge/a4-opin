from django.db.models.signals import post_delete, post_init, post_save
from django.dispatch import receiver

from euth.contrib import services

from .models import Project


@receiver(post_init, sender=Project)
def backup_image_path(sender, instance, **kwargs):
    instance._current_image_file = instance.image


@receiver(post_save, sender=Project)
def delete_old_image(sender, instance, **kwargs):
    if hasattr(instance, '_current_image_file'):
        if instance._current_image_file != instance.image:
            services.delete_images([instance._current_image_file])


@receiver(post_delete, sender=Project)
def delete_images_for_project(sender, instance, **kwargs):
    services.delete_images([instance.image])
