from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.models import User
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
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('chat:index')
        else:
            print(form.errors)
    return render(request,'chat/signin.html',{})

def sign_up(request):
    error_messages = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat:index')
        else:
            error_messages = form.errors.values
    return render(request,'chat/signup.html',{'error_messages':error_messages})

@login_required(login_url='/sign-in/')
def sign_out(request):
    logout(request)
    return redirect('chat:index')