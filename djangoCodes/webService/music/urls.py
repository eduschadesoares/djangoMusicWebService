from django.conf.urls import url
from . import views


app_name = 'music'

urlpatterns = [
    url(r'^musics/$', views.MusicList.as_view(), name='music-list'),

]