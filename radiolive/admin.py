from django.contrib import admin

from .models import Playlist, SongList

admin.site.register(Playlist)
admin.site.register(SongList)
