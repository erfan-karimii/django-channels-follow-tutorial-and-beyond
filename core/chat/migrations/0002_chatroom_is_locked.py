# Generated by Django 4.1.3 on 2023-03-31 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='is_locked',
            field=models.BooleanField(default=False),
        ),
    ]