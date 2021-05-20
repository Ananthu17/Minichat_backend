import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack   
import api_backend.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mc_backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            api_backend.routing.websocket_urlpatterns
        )
    )
})