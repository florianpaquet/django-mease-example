from rest_framework import generics

from .models import Board
from .models import Message
from .serializers import BoardSerializer
from .serializers import MessageSerializer
from .serializers import MessageListSerializer


class ListCreateBoardAPIView(generics.ListCreateAPIView):
    model = Board
    serializer_class = BoardSerializer


class CreateMessageAPIView(generics.CreateAPIView):
    model = Message
    serializer_class = MessageSerializer


class ListMessageAPIView(generics.ListAPIView):
    serializer_class = MessageListSerializer

    def get_queryset(self):
        board_id = self.kwargs['board_id']
        return Message.objects.filter(board__pk=board_id)
