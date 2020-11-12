from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from games.service import GamesFilter
from .models import GamesModel, PostModel
from .serializers import (
    GamesListSerializers,
    GameDetailSerializers,
    PostCreateSerializers,
    PostListSerializers,
    PostDetailSerializers)


class GamesListView(ListAPIView):
    """Список фильмов"""
    queryset = GamesModel.objects.all()
    serializer_class = GamesListSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GamesFilter
    permission_classes = [permissions.IsAuthenticated]


class GamesDetailView(RetrieveAPIView):
    """Список фильмов"""
    queryset = GamesModel.objects.all()
    serializer_class = GameDetailSerializers


class PostCreateView(CreateAPIView):
    """Добавления поста к игре"""
    serializer_class = PostCreateSerializers


class PostListView(ListAPIView):
    """Вывод всех постов"""
    queryset = PostModel.objects.all()
    serializer_class = PostListSerializers


class PostDetailView(RetrieveAPIView):
    """Вывод описания поста"""
    queryset = PostModel.objects.all()
    serializer_class = PostDetailSerializers
