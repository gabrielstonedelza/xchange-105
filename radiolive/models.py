from django.db import models
from PIL import Image
from django.core.validators import FileExtensionValidator
from django.template.defaultfilters import slugify
from django.urls import reverse


class Playlist(models.Model):
    playlist_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, default="")
    poster = models.ImageField(upload_to='posters', blank=True, default="1.png")
    views = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.playlist_title

    def get_absolute_url(self):
        return reverse("playlist_detail", args={self.slug})

    def save(self, *args, **kwargs):
        value = self.playlist_title
        self.slug = slugify(value)
        super().save(*args, **kwargs)

        img = Image.open(self.poster.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail = output_size
            img.save(self.poster.path)


class SongList(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song_list = models.FileField(upload_to="playlists")
    title = models.CharField(max_length=200, default='')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.playlist.playlist_title

    def save(self, *args, **kwargs):
        value = self.song_list
        self.title = slugify(value)
        super().save(*args, **kwargs)

    def get_songlist(self):
        if self.song_list:
            return "http://127.0.0.1:8000" + self.song_list.url
        return ''

    def get_title(self):
        string = self.title
        new_string = string.replace('mp3', '')
        without_mp3 = new_string.replace('-', ' ')
        without_slash = without_mp3.replace('_', ' ')
        return without_slash
