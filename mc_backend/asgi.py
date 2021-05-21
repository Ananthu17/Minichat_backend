import os
from django.conf.urls import url

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mc_backend.settings')

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack   
import api_backend.routing


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            api_backend.routing.websocket_urlpatterns
        )
    )
})
