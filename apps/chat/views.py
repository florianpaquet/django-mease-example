from django.views.generic import TemplateView


class ChatView(TemplateView):
    """
    Char index
    """
    template_name = 'chat/index.html'
