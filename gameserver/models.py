from django.db import models

class WebsocketMessage(models.Model):
  session_id = models.UUIDField(editable=False)
  client_id = models.UUIDField(editable=False)
  timestamp = models.BigIntegerField(editable=False)
  json = models.JSONField()

  class Meta:
    indexes = [models.Index(fields=['session_id', 'timestamp'])]

  def __str__(self) -> str:
    return f'[ session: {self.session_id} client: {self.client_id} timestamp: {self.timestamp} ]'

class GameSave(models.Model):
  # It seems django doesn't do composite primary keys, so instead I must add a constraint
  session_id = models.UUIDField(editable=False)
  client_id = models.UUIDField(editable=False)
  timestamp = models.BigIntegerField(editable=False)
  serialized_save = models.TextField(editable=False)

  class Meta:
    constraints = [models.UniqueConstraint(fields = ['session_id', 'client_id'], name='UQ_GAMESAVE_SESSION_ID_CLIENT_ID')]