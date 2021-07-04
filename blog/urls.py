from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('playlist/<str:slug>/', views.playlist_detail, name="playlist_detail"),
    path('podcasts/', views.podcasts, name='podcasts'),
    path('about', views.about, name='about'),
    path('create_playlist/', views.create_playlist, name="create_playlist"),
    path('success/', views.success, name='success'),
    path('add2playlist/', views.add_to_playlist, name='add2playlist')
]
