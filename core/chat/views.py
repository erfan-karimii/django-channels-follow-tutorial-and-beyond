from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.http import JsonResponse

from .models import ChatRoom , Chat
# Create your views here.

def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    room, created = ChatRoom.objects.get_or_create(name=room_name)
    chats = Chat.objects.filter(room=room)

    ano_user_name = ''
    if request.user.is_anonymous:
        ano_user_name = request.COOKIES.get('anonymoususer')

    if created:
        if request.user.is_authenticated:
            room.creator_username = request.user.username
        else:
            room.creator_username = ano_user_name
        room.save()
    else:
        # check id room is locked and if user is not creator user dont allow to go to the room
        if room.is_locked and \
            room.creator_username != request.user.username and \
            room.creator_username != ano_user_name:
            messages.error(request,'در این اتاق بسته است.')
            return redirect('chat:index')

    context =  {
        "room": room,
        'chats':chats,
        'ano_user_name' : ano_user_name, 
    }
    return render(request, "chat/room.html",context )

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

def change_lock_room(request):
    room_id = request.GET.get('room_id')
    room = ChatRoom.objects.get(id=room_id)
    if room.is_locked :
        room.is_locked = False
        msg = 'در باز شد!'
    else :
        room.is_locked = True
        msg = 'در بسته شد!'
    room.save()
    return JsonResponse({'msg':msg})
