# Generated by Django 4.0.1 on 2022-01-16 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameserver', '0004_delete_gamesession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesave',
            name='timestamp',
            field=models.BigIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='websocketmessage',
            name='timestamp',
            field=models.BigIntegerField(editable=False),
        ),
    ]
