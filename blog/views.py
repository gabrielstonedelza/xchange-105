from django.shortcuts import render, redirect, get_object_or_404
from radiolive.models import Playlist, SongList
from .forms import PlayListForm, SongListForm
from django.contrib import messages
import filetype


def csrf_failure(request, reason=""):
    return render(request, "blog/403_csrf.html")


def home(request):
    playlists = Playlist.objects.all().order_by('-date_created')

    context = {
        "playlists": playlists
    }

    return render(request, "blog/playlists.html", context)


def playlist_detail(request, slug):
    deplaylist = get_object_or_404(Playlist, slug=slug)
    song_lists = SongList.objects.filter(playlist=deplaylist).order_by('-date_created')

    if deplaylist:
        deplaylist.views += 1
        deplaylist.save()

    context = {
        "deplaylist": deplaylist,
        "song_lists": song_lists
    }

    return render(request, "blog/playlist_detail.html", context)


def podcasts(request):
    return render(request, "blog/podcast.html")


def about(request):
    return render(request, "blog/about.html")


def create_playlist(request):
    if request.method == "POST":
        form = PlayListForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('playlist_title')
            poster = form.cleaned_data.get('poster')
            Playlist.objects.create(playlist_title=title, poster=poster)
            messages.success(request, f'successfully created your playlist')
            return redirect('add2playlist')
    else:
        form = PlayListForm()

    context = {
        "form": form
    }

    return render(request, "blog/create_playlist.html", context)


def add_to_playlist(request):
    if request.method == "POST":
        form = SongListForm(request.POST, request.FILES)
        if form.is_valid():
            playlist = form.cleaned_data.get('playlist')
            song_list = request.FILES.getlist('song_list')

            for song in song_list:
                SongList.objects.create(playlist=playlist, song_list=song)
            messages.success(request, f'songs have been added to your playlist')
            return redirect('success')
    else:
        form = SongListForm()

    context = {
        "form": form
    }
    return render(request, "blog/addto_playlist.html", context)


def success(request):
    return render(request, "blog/success.html")
