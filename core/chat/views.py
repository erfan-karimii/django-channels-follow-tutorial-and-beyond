from django.shortcuts import render
from .models import ChatRoom , Chat
# Create your views here.

def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    room = ChatRoom.objects.filter(name=room_name).first()
    chats = []
    if room:
        chats = Chat.objects.filter(room=room)
    else:
        room = ChatRoom(name=room_name)
        room.save()

    return render(request, "chat/room.html", {"room_name": room_name,'chats':chats})

def sign_in(request):
    
    return render(request,'chat/signin.html',{})