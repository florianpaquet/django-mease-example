# -*- coding: utf-8 -*-
from djmease import mease
from django.conf import settings

from ..websocket import make_message

DATETIME_FORMAT = getattr(settings, 'CHAT_DATETIME_FORMAT')


# ---- Senders

@mease.sender(routing='messages.created')
def message_created(routing, clients_list, message):
    """
    Sends messages on message creation
    """
    msg = make_message('messages.created', {
        'admin': message.admin,
        'notice': False,
        'created': message.created.strftime(DATETIME_FORMAT),
        'username': message.username,
        'content': message.content,
    })

    for client in clients_list:
        if client.storage['subscription'] == message.board.pk:
            client.send(msg)
