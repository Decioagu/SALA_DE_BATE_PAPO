# SALA_DE_BATE_PAPO

- Projeto de comunicação em tempo real (WebSockets) em processos assíncrono:

- WebSockets:  é uma tecnologia que permite comunicação bidirecional e em tempo real entre o navegador (frontend) e o servidor (backend) através de uma conexão persistente.

- HTTP tradicional:
        - Cada requisição do cliente abre uma conexão, envia a mensagem, recebe a resposta e fecha a conexão.
        - Exemplo: o usuário envia um formulário → o servidor responde → conexão encerrada.

    - WebSocket:
        - O cliente abre uma conexão e mantém ela aberta. Assim, o servidor pode enviar dados para o cliente a qualquer momento, sem precisar esperar por uma requisição.
        -  É ideal para:
            - Chats em tempo real 💬
            - Notificações instantâneas 🔔
            - Jogos multiplayer 🎮
            - Atualizações em dashboards 

- Escolha nome para sua sala de bate papo, o nome da sala não pode conter caracteres especias, nome acentuado ou espaço para funcionar corretamente:
![Nome da sala de bate papo](<imagem/nome da sala.png>)

- Copie e cole  o endereço URL do seu navegador em uma nova pagina ou em um outro navegador para conversar na mesma sala de bate papo:
![Sala de bate papo](imagem/sala.png) 

- Roteiro de construção:

- pip install django django-bootstrap4  channels  channels-redis daphne whitenoise

    - django: Framework web de alto nível para desenvolvimento rápido de aplicações web seguras e escaláveis.

    - django-bootstrap4: Biblioteca que facilita a integração do framework Bootstrap 4 com templates do Django.

    - channels: expande o Django para trabalhar com ASGI (aplicações assíncronas), Django sozinho só aceita HTTP síncrono (com WSGI), Channels é necessário para trabalhar com tempo real e comunicação persistente.

    - channels-redis: funciona como um intermediário para essa troca de multiplas mensagens, auxiliando a biblioteca "django-channels" para permitir que múltiplos processos no Django.

    - daphne: é o servidor padrão recomendado para rodar aplicações Django que utilizam Django Channels, que adiciona suporte a WebSockets e outras funcionalidades assíncronas no Django.

    - whiteNoise: é uma biblioteca Python que “ensina” seu servidor ASGI/WSGI (Daphne, Uvicorn, Gunicorn) a servir arquivos estáticos diretamente.

- Criar projeto:
    - django-admin startproject realtime

- Criar aplicativo:
    - python manage.py startapp chat

- Aplicar migração de estrutura de banco de dados:
    - python manage.py migrate

- Para rodar  WebSocket com Channels utilize "Daphne":
    - daphne realtime.asgi:application

- Abrir pagina: 
    - http://127.0.0.1:8000/

- Arquivo:
    - chat:
        - templates:
            - __index.html__: Pagina HTML
            - __sala.html__: Pagina HTML
        - __views.py__: Adição de requisições para templates (Paginas HTML)
        - __routing.py__: Rotas e conexões tratadas por WebSockets (__consumers.py__)
        - __consumers.py__: Élo de ligação entre WebSockets e a aplicação Django
        - __chat_urls.py__: Rotas da apalicação (__views.py__)
    - realtime:
        - __asgi.py__: Gerencia rotas e serviços assicrono como Daphne ou Uvicorn (__routing.py__)
        - __urls.py__: Gerenciador de rotas das aplicações (__chat_urls.py__)
        - __settings.py__: Configuração ASGI (aplicações assíncronas)   


