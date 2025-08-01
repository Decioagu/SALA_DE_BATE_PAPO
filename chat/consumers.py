from channels.generic.websocket import AsyncWebsocketConsumer
import json

'''
- Sala de Bate-Papo (Chat)
    - Consumer é o élo de ligação entre comunicação em tempo real (WebSockets) e a aplicação Django.
        - É uma classe que define como o WebSocket irá se comportar.
        - É responsável por receber e enviar mensagens através do WebSocket.
        - É uma classe assíncrona que herda de AsyncWebsocketConsumer.
        - Define métodos para conectar, desconectar e receber mensagens.
        - Utiliza o channel layer para enviar mensagens para grupos de WebSockets.
        - Permite que múltiplos clientes se conectem e recebam mensagens em tempo real
'''
#21 Consumer para o Chat (navegador e aplicação)
class ChatConsumer(AsyncWebsocketConsumer):

    # Entrar na Sala
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['nome_sala'] # recuperar nome da sala da URL
        self.room_group_name = f'chat_{self.room_name}' # renomeia self.room_name

        # aguarda entrar na sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept() # aceita a conexão do WebSocket

    # Sair da Sala
    async def disconnect(self, code):
        # aguarda sair da sala
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Enviara mensagem do WebSocket para a sala
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        mensagem = text_data_json['mensagem']

        # Envia a mensagem para a sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': mensagem
            }
        )

    # Recebe a mensagem do grupo da sala
    async def chat_message(self, event):
        mensagem = event['message']

        # Envia a mensagem para o WebSocket
        await self.send(text_data=json.dumps({
            'mensagem': mensagem
        }))
