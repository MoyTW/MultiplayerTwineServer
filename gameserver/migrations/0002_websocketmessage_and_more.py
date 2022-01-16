# Generated by Django 4.0.1 on 2022-01-14 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameserver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsocketMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.UUIDField(editable=False)),
                ('client_id', models.UUIDField(editable=False)),
                ('timestamp', models.IntegerField(editable=False)),
                ('json', models.JSONField()),
            ],
        ),
        migrations.AddIndex(
            model_name='websocketmessage',
            index=models.Index(fields=['session_id', 'timestamp'], name='gameserver__session_576201_idx'),
        ),
    ]
