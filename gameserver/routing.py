from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
  re_path(r'ws/(?P<session_id>[0-9a-f]{8}\-[0-9a-f]{4}\-4[0-9a-f]{3}\-[89ab][0-9a-f]{3}\-[0-9a-f]{12})/$', consumers.ChatConsumer.as_asgi()),
]