# -*- coding: utf-8 -*-
from django.db import models


class Board(models.Model):
    """
    Board containing messages
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(self.name)


class Message(models.Model):
    """
    Simple message model
    """
    admin = models.BooleanField(default=False)
    board = models.ForeignKey(Board)
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.content

    def __unicode__(self):
        return unicode(self.content)
