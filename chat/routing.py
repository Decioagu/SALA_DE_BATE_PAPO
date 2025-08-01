from django.urls import re_path #21 Expressão regular

from chat.consumers import ChatConsumer #21 Gerenciar as conexões WebSocket

#21 Define as rotas para o WebSocket
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+)/$', ChatConsumer.as_asgi()), 
]
