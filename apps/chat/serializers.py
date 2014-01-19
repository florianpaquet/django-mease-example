from django.conf import settings
from rest_framework import serializers

from .models import Board
from .models import Message

DATETIME_FORMAT = getattr(settings, 'CHAT_DATETIME_FORMAT')


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message


class MessageListSerializer(MessageSerializer):
    created = serializers.SerializerMethodField('get_created')

    def get_created(self, obj):
        return obj.created.strftime(DATETIME_FORMAT)
