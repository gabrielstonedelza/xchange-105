from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Playlist, SongList
from .serializers import PlaylistSerializer, SongListSerializer


@api_view(['GET'])
def get_playlist(request):
    playlists = Playlist.objects.all().order_by('-date_created')
    serializer = PlaylistSerializer(playlists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_songlist(request):
    songlists = SongList.objects.all().order_by('-date_created')
    serializer = SongListSerializer(songlists, many=True)
    return Response(serializer.data)
