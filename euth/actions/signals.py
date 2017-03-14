from django.apps import apps
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from adhocracy4.projects.models import Project
from euth.actions import emails

from . import verbs
from .models import Action


def add_action(sender, instance, created, **kwargs):
    verb = verbs.CREATE if created else verbs.UPDATE
    actor = instance.creator

    action = Action(
        actor=actor,
        verb=verb,
        action_object=instance
    )

    if hasattr(instance, 'project') and instance.project.__class__ is Project:
        action.project = instance.project
        action.target = instance.project

    if hasattr(instance, 'content_object'):
        action.target = instance.content_object

    action.save()


for app, model in settings.ACTIONABLE:
    post_save.connect(add_action, apps.get_model(app, model))


def notify_creator(action):
    if hasattr(action.target, 'creator'):
        creator = action.target.creator
        if creator.get_notifications and not creator == action.actor:
            emails.notify_users_on_create_action(action, [creator])


def notify_moderators(action):
    if action.target_content_type.model_class() is Project:
        recipients = action.project.moderators \
                                   .exclude(id=action.actor.id) \
                                   .filter(get_notifications=True) \
                                   .values_list('email', flat=True)

        emails.notify_users_on_create_action(action, recipients)


@receiver(post_save, sender=Action)
def send_notification(sender, instance, created, **kwargs):

    if instance.verb == verbs.CREATE:
        notify_creator(instance)
        notify_moderators(instance)
    if instance.verb == verbs.COMPLETE:
        emails.notify_followers_on_almost_finished(instance.project)
