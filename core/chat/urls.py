from django.urls import path

from . import views

app_name= 'chat'

urlpatterns = [
    path("", views.index, name="index"),
    path("sign-in/", views.sign_in, name="sign-in"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path("sign-out/", views.sign_out, name="sign-out"),
    path("change_lock/", views.change_lock_room, name="change_lock"),
    path("<str:room_name>/", views.room, name="room"),
]