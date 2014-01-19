# -*- coding: utf-8 -*-
import mease
from django.conf import settings

from ..websocket import make_message

DATETIME_FORMAT = getattr(settings, 'CHAT_DATETIME_FORMAT')


# ---- Senders

@mease.sender(channels=['messages.created'])
def message_created(channel, clients_list, message):
    """
    Sends messages on message creation
    """
    msg = make_message('messages.created', {
        'admin': message.admin,
        'created': message.created.strftime(DATETIME_FORMAT),
        'username': message.username,
        'content': message.content,
    })

    for client in clients_list:
        if client.storage['subscription'] == message.board.pk:
            client.send(msg)
