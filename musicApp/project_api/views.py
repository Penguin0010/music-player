from .serializers import *
from rest_framework import response, reverse
from rest_framework.views import APIView  # used for APIRoot
from rest_framework import permissions  # used to set permissions on api access
from .permissions import IsStaffOrNot  # custom permission for accessing api
# using ModelViewSet class to include all the HTTP protocol methods in one CBV
from rest_framework import viewsets
from musicApp.models import *

# API: CBV for getting all articles
class APISongsViewSet(viewsets.ModelViewSet):

    queryset = Song.objects.order_by('-id')
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)


# API: CBV for getting all editors
class APIPlaylistsViewSet(viewsets.ModelViewSet):

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)


# API: CBV for getting all comments
class APIFavouritesViewSet(viewsets.ModelViewSet):

    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)


# API: CBV for getting all users
class APIRecentsViewSet(viewsets.ModelViewSet):

    queryset = Recent.objects.all()
    serializer_class = RecentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)

class APICommentsViewSet(viewsets.ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)
