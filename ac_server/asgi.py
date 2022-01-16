"""
ASGI config for ac_server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import django

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ac_server.settings')
django.setup()

# What the fresh hell is this!?
# So! If put the import before django.setup() it will fail the import, because models require that Stuff executed in
# django.setup() happen (I'm indistinct on the details here; it has something to do with apps being "ready")
import gameserver.routing

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(URLRouter(gameserver.routing.websocket_urlpatterns)),
})
