from django import forms
from radiolive.models import Playlist, SongList


class PlayListForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['playlist_title', 'poster']


class SongListForm(forms.ModelForm):
    song_list = forms.FileField(label="Select songs", widget=forms.FileInput(
        attrs={"class": "form-control", "multiple": "multiple", "name": "song_list"}))

    class Meta:
        model = SongList
        fields = ['playlist', 'song_list']
