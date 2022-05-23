from cgitb import lookup
from dataclasses import field
from rest_framework import serializers
from musicApp.models import *


class SongSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Playlist
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['song'] = SongSerializer(read_only=True)
        return super().to_representation(instance)



class FavouriteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Favourite
        fields = '__all__'
    def to_representation(self, instance):
        self.fields['song'] = SongSerializer(read_only=True)
        return super().to_representation(instance)


class RecentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Recent
        fields = '__all__'

class CommentsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'
