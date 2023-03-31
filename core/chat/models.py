from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=122,null=True)
    room = models.ForeignKey('ChatRoom',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content


class ChatRoom(models.Model):
    name = models.CharField(max_length=22)
    creator_username = models.CharField(max_length=120,null=True)
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
