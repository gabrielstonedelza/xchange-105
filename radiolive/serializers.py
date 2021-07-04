from rest_framework import serializers
from .models import Playlist, SongList


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'playlist_title']


class SongListSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('playlist_title')

    class Meta:
        model = SongList
        fields = ['id', 'title', 'playlist', 'song_list', 'get_songlist', 'get_title']

    def playlist_title(self, songlist):
        title = songlist.playlist.playlist_title
        return title
