from django.urls import path

from . import views

app_name= 'chat'

urlpatterns = [
    path("", views.index, name="index"),
    path("sign-in/", views.sign_in, name="sign-in"),
    path("<str:room_name>/", views.room, name="room"),
]