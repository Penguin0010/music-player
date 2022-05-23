from .serializers import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.mixins import *
from rest_framework.generics import *
from rest_framework import permissions # new import
from .permissions import IsStaffOrNot
# API: CBV for getting all articles
class APISongsListView(ListCreateAPIView):
    queryset = Song.objects.order_by('-id')
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]
    def get_serializer(self, *args, **kwargs):

        if isinstance(kwargs.get('data', {}), list):
            kwargs['many']=True
        return super(ListCreateAPIView,self).get_serializer(*args, **kwargs)

class APISongsDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.order_by('-id')
    serializer_class= SongSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]
    def get_serializer(self, *args, **kwargs):
        kwargs['partial']=True
        return super(RetrieveUpdateDestroyAPIView, self).get_serializer(*args, **kwargs)

# API: CBV for getting all editors
class APIPlaylistsListView(ListCreateAPIView):

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many']=True
        return super(ListCreateAPIView,self).get_serializer(*args, **kwargs)


# API: CBV for getting particular editor & manipulating over it
# there are other options:
#      RetrieveDestroy-, RetrieveUpdate-, Retrieve-, Update-, DestroyAPIView
class APIPlaylistDetailsView(RetrieveUpdateDestroyAPIView):

    queryset = Playlist.objects.all()
    serializer_class= PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        kwargs['partial']=True
        return super(RetrieveUpdateDestroyAPIView, self).get_serializer(*args, **kwargs)

# API: CBV for getting all comments
class APIFavouritesListView(ListCreateAPIView):

    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many']=True
        return super(ListCreateAPIView,self).get_serializer(*args, **kwargs)


# API: CBV for getting particular comment & manipulating over it
# there are other options:
#      RetrieveDestroy-, RetrieveUpdate-, Retrieve-, Update-, DestroyAPIView
class APIFavouriteDetailsView(RetrieveUpdateDestroyAPIView):

    queryset = Favourite.objects.all()
    serializer_class= FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        kwargs['partial']=True
        return super(RetrieveUpdateDestroyAPIView, self).get_serializer(*args, **kwargs)

# API: CBV for getting all users
class APIRecentsListView(ListCreateAPIView):

    queryset = Recent.objects.all()
    serializer_class = RecentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many']=True
        return super(ListCreateAPIView,self).get_serializer(*args, **kwargs)


# API: CBV for getting particular user & manipulating over it
# there are other options:
#      RetrieveDestroy-, RetrieveUpdate-, Retrieve-, Update-, DestroyAPIView
class APIRecentDetailsView(RetrieveUpdateDestroyAPIView):

    queryset = Recent.objects.all()
    serializer_class= RecentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        kwargs['partial']=True
        return super(RetrieveUpdateDestroyAPIView, self).get_serializer(*args, **kwargs)

class APICommentsListView(ListCreateAPIView):

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many']=True
        return super(ListCreateAPIView,self).get_serializer(*args, **kwargs)


# API: CBV for getting particular user & manipulating over it
# there are other options:
#      RetrieveDestroy-, RetrieveUpdate-, Retrieve-, Update-, DestroyAPIView
class APICommentsDetailsView(RetrieveUpdateDestroyAPIView):

    queryset = Comments.objects.all()
    serializer_class= CommentsSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        kwargs['partial']=True
        return super(RetrieveUpdateDestroyAPIView, self).get_serializer(*args, **kwargs)