from rest_framework import routers

from .views import *
from .viewsets import *

default_router = routers.DefaultRouter()
default_router.register(r'songs', APISongsViewSet)
default_router.register(r'playlist', APIPlaylistsViewSet)
default_router.register(r'recent', APIRecentsViewSet)
default_router.register(r'favourite', APIFavouritesViewSet)
default_router.register(r'comments', APICommentsViewSet)
