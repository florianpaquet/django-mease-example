from django.conf.urls import url
from django.conf.urls import patterns

from .views import ChatView
from .api_views import ListCreateBoardAPIView
from .api_views import ListMessageAPIView
from .api_views import CreateMessageAPIView


urlpatterns = patterns(
    '',
    url(
        r'^$',
        ChatView.as_view()),

    url(
        r'^api/boards$',
        ListCreateBoardAPIView.as_view(),
        name='chat_boards_listcreate'),
    url(
        r'^api/messages$',
        CreateMessageAPIView.as_view(),
        name='chat_messages_create'),
    url(
        r'^api/messages/(?P<board_id>\d+)$',
        ListMessageAPIView.as_view(),
        name='chat_messages_list'),
)
