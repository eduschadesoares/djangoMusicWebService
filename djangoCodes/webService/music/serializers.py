from rest_framework import serializers
from .models import (Music,
                     Band,
                     Record,
                     Genre,
                     Playlist,
                     )

class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'