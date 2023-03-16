from django.contrib import admin
from .models import Chat , ChatRoom


class CustomChat(admin.ModelAdmin):
    list_display = ('room','username','content','timestamp')

admin.site.register(Chat,CustomChat)
admin.site.register(ChatRoom)
