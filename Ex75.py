import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from xat import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webxat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter({
            # Aquesta és la ruta per al WebSocket, gestionada pel consumidor de WebSocket
            "ws/xat/": consumers.XatConsumer.as_asgi(),
        })
    ),
})
