from django.urls import path
from . import views

urlpatterns = [
    path('playlists/', views.get_playlist),
    path('songlist/', views.get_songlist)
]
