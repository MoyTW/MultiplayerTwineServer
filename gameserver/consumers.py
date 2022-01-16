import json
import time
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from gameserver.models import GameSave, WebsocketMessage

class ChatConsumer(WebsocketConsumer):
  def connect(self):
    self.session_id = self.scope['url_route']['kwargs']['session_id']
    self.session_id_group_name = f'channel_{self.session_id}'

    async_to_sync(self.channel_layer.group_add)(
      self.session_id_group_name,
      self.channel_name
    )

    self.accept()
  
  def disconnect(self, code):
    print(code)
    async_to_sync(self.channel_layer.group_discard)(
      self.session_id_group_name,
      self.channel_name
    )
  
  def receive(self, text_data, bytes_data=None):
    text_data_map = json.loads(text_data)
    server_ms = int(time.time() * 1000)
    text_data_map['server_timestamp_ms'] = server_ms

    print(text_data_map)

    if text_data_map['type'] == 'CATCH_UP':
      try:
        save = GameSave.objects.get(session_id__exact=self.session_id, client_id__exact=text_data_map['clientId'])
        messages = WebsocketMessage.objects.filter(session_id__exact=self.session_id, timestamp__gt=save.timestamp)
      except GameSave.DoesNotExist:
        save = None
        messages = WebsocketMessage.objects.filter(session_id__exact=self.session_id, timestamp__gt=text_data_map['catchupStartMs'])
      # TODO: this is a little farcical tbh
      content = {'type': 'CATCH_UP', 'messages': [json.loads(m.json) for m in messages], 'server_timestamp_ms': server_ms}
      if save:
        content['serialized_save'] = save.serialized_save
      self.send(text_data=json.dumps(content))
    elif text_data_map['type'] == 'AUTOSAVE':
      try:
        GameSave.objects.get(session_id__exact=self.session_id, client_id__exact=text_data_map['clientId']).delete()
      except GameSave.DoesNotExist:
        pass
      GameSave(session_id=self.session_id, client_id=text_data_map['clientId'], timestamp=server_ms, serialized_save=text_data_map['serializedSave']).save()
    else:
      row = WebsocketMessage(session_id=self.session_id, client_id=text_data_map['clientId'], timestamp=server_ms, json=text_data)
      row.save()

      async_to_sync(self.channel_layer.group_send)(
        self.session_id_group_name,
        {
          'type': 'chat_message',
          'message': text_data_map
        }
      )

  def chat_message(self, event):
    print(event)
    data_str = json.dumps(event['message'])
    self.send(text_data=data_str)