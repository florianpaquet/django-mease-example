import mease
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Board
from .models import Message


@receiver(post_save, sender=Board)
def board_created(sender, instance, *args, **kwargs):
    mease.publish('boards.created', board=instance)


@receiver(post_save, sender=Message)
def message_created(sender, instance, *args, **kwargs):
    mease.publish('messages.created', message=instance)
